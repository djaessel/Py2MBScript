import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts


ColumnLayout {
  id: itemManagerRoot
  spacing: 0

  property var curItem: null

  onCurItemChanged: {
        for (var kchild in flagsGridLayout.children) {
		flagsGridLayout.children[kchild].checked = false
	}

	for (var kchild in force_show_row.children) {
		force_show_row.children[kchild].checked = false
	}

	propertyFlagsBtn.clicked()

	type_cbb.currentIndex = 0
	attach_cbb.currentIndex = 0
	custom_kill_info_cbb.currentIndex = 0

	var idx = custom_kill_info_cbb.model.indexOf(curItem.custom_kill_info)
	if (idx > 0){
		custom_kill_info_cbb.currentIndex = idx
	}

	for (var kflag in curItem.flags) {
		var flag = curItem.flags[kflag]
		for (var kchild in flagsGridLayout.children) {
			var checkx = "itp_" + flagsGridLayout.children[kchild].text.replace(' ', '_').toLowerCase()
			if (checkx == flag) {
				flagsGridLayout.children[kchild].checked = true
			}
		}

                for (var kchild in force_show_row.children) {
                        var checkx = "itp_" + force_show_row.children[kchild].text.replace(' ', '_').toLowerCase()
                        if (checkx == flag) {
                                force_show_row.children[kchild].checked = true
                        }
                }

		var typeFlag = flag.replace("itp_type_", "")
		if (type_cbb.model.includes(typeFlag)) {
			type_cbb.currentIndex = type_cbb.model.indexOf(typeFlag)
		}

                var attachFlag = flag.replace("itp_", "")
                if (attach_cbb.model.includes(attachFlag)) {
                        attach_cbb.currentIndex = attach_cbb.model.indexOf(attachFlag)
                }
	}
  }

  RowLayout {
        id: tabxs
        spacing: 0
	Button {
                id: propertyFlagsBtn
		flat: true
		palette.buttonText: "black"
		palette.button: "darkgrey"
		text: "Property Flags"
        	background: Rectangle {
            		implicitWidth: 100
            		implicitHeight: 25
            		border.width: propertyFlagsBtn.activeFocus ? 3 : 2
            		border.color: "black"
            		radius: 2
            		gradient: Gradient {
                		GradientStop { position: 0 ; color: propertyFlagsBtn.pressed ? "#ccc" : "#eee" }
                		GradientStop { position: 1 ; color: propertyFlagsBtn.pressed ? "#aaa" : "#ccc" }
            		}
    		}
                onClicked: {
                	for (var kchild in tabxs.children) {
                		tabxs.children[kchild].enabled = true
	                }
			propertyFlagsBtn.enabled = false
                        property_flags_gb.visible = true
			capability_flags_gb.visible = false
                }
	}
	Button {
		id: capabilityFlagsBtn
		flat: true
		palette.buttonText: "black"
		palette.button: "darkgrey"
                background: Rectangle {
                        implicitWidth: 100
                        implicitHeight: 25
                        border.width: capabilityFlagsBtn.activeFocus ? 3 : 2
                        border.color: "black"
                        radius: 2
                        gradient: Gradient {
                                GradientStop { position: 0 ; color: capabilityFlagsBtn.pressed ? "#ccc" : "#eee" }
                                GradientStop { position: 1 ; color: capabilityFlagsBtn.pressed ? "#aaa" : "#ccc" }
                        }
                }

		text: "Capability Flags"
                onClicked: {
                        for (var kchild in tabxs.children) {
                                tabxs.children[kchild].enabled = true
                        }
                        capabilityFlagsBtn.enabled = false
                        property_flags_gb.visible = false
			capability_flags_gb.visible = true
                }
	}
	Button {
		id: saveBtn
                flat: true
                palette.buttonText: "black"
                palette.button: "darkgrey"
                background: Rectangle {
                        implicitWidth: 100
                        implicitHeight: 25
                        border.width: capabilityFlagsBtn.activeFocus ? 3 : 2
                        border.color: "black"
                        radius: 2
                        gradient: Gradient {
                                GradientStop { position: 0 ; color: capabilityFlagsBtn.pressed ? "#ccc" : "#eee" }
                                GradientStop { position: 1 ; color: capabilityFlagsBtn.pressed ? "#aaa" : "#ccc" }
                        }
                }
                text: "Save"
		onClicked: {
			var xxxxx = textHandler.getText()
			var idxs = textHandler.getText().indexOf("<p>" + coolcombo.model[coolcombo.currentIndex].text + " = ") + 3
			var idxFirst = idxs

			xxxxx = savePropertyFlags(xxxxx, idxs, idxFirst)

			textHandler.setText(xxxxx)
			textArea.text = textHandler.getText()
		}

		function savePropertyFlags(xxxxx, idxs, idxFirst) {
                        var xs = textHandler.getText().substring(idxs)
                        xs = xs.substring(0, xs.indexOf("</p>"))
                        xxxxx = xxxxx.replace(xs, "")
                        var xs2 = textHandler.getText().substring(idxs)
                        while (idxs > 2) {
                                idxs = xs2.indexOf("<p>" + coolcombo.model[coolcombo.currentIndex].text + ".") + 3
                                if (idxs > 2) {
                                        xs2 = xs2.substring(idxs)
                                        xs = xs2.substring(0, xs2.indexOf("</p>"))
                                        xxxxx = xxxxx.replace(xs, "")
                                }
                        }
			xxxxx = xxxxx.replace("<p></p>", "")


                        var newText = "<p>" + curItem.id + " = Item(\"" + curItem.id + "\", \"" + curItem.name + "\", " + curItem.price + ")</p>"

			for (var kmesh in curItem.meshes) {
				newText += "<p>" + curItem.id + ".add_mesh(ItemMesh(\"" + curItem.meshes[kmesh].id + "\""
				if (curItem.meshes[kmesh].modifier != "0") {
					newText += "," + curItem.meshes[kmesh].modifier
				}
				newText += "))</p>"
			}

			if (type_cbb.currentIndex > 0) {
				newText += "<p>" + curItem.id + ".set_type(ItemType." + type_cbb.model[type_cbb.currentIndex].toUpperCase() + ")</p>"
			}

                        if (custom_kill_info_cbb.currentIndex > 0) {
                                newText += "<p>" + curItem.id + ".custom_kill_info = \"" + custom_kill_info_cbb.model[custom_kill_info_cbb.currentIndex] + "\"</p>"
                        }

                        for (var kchild in force_show_row.children) {
                            if (force_show_row.children[kchild].checked){
                                newText += "<p>" + curItem.id + ".add_flag(ItemFlag." + force_show_row.children[kchild].flagValue + ")</p>"
                            }
                        }

                        for (var kchild in flagsGridLayout.children) {
                            if (flagsGridLayout.children[kchild].checked){
                                newText += "<p>" + curItem.id + ".add_flag(ItemFlag." + flagsGridLayout.children[kchild].flagValue + ")</p>"
                            }
                        }


                        xxxxx = xxxxx.slice(0, idxFirst) + newText + xxxxx.slice(idxFirst)
			return xxxxx
		}
	}
  }

  GroupBox {
    id: property_flags_gb

   ColumnLayout {

    RowLayout {
	id: typesx

        Label {
                text: "Type:"
        }

    	ComboBox {
		id: type_cbb
		Layout.minimumWidth: 200
		model: [
		"none",
		"horse",
		"one_handed_wpn",
		"two_handed_wpn",
		"polearm",
		"arrows",
		"bolts",
		"shield",
		"bow",
		"crossbow",
		"thrown",
		"goods",
		"head_armor",
		"body_armor",
		"foot_armor",
		"hand_armor",
		"pistol",
		"musket",
		"bullets",
		"animal",
		"book",
		]
    	}


        Label {
                text: "Attach:"
        }

	ComboBox {
		id: attach_cbb
		Layout.minimumWidth: 200
		model: [
		"none",
		"force_attach_left_hand",
		"force_attach_right_hand",
		"force_attach_left_forearm",
		"attach_armature",
		]
	}


        Label {
                text: "Custom Kill Info:"
        }

	ComboBox {
		id: custom_kill_info_cbb
		Layout.minimumWidth: 200
		model: [
		"none",
		"ico_custom_1",
		"ico_custom_2",
		"ico_custom_3",
		"ico_custom_4",
		"ico_custom_5",
		"ico_custom_6",
		"ico_custom_7",
		]
	}

    }


    GroupBox {
	id: force_show_gb
	title: "Force Show"

     RowLayout {
	id: force_show_row
	CheckBox {
		id: force_show_left_hand_cb
		text: "Left Hand"
		property var flagValue: "FORCE_SHOW_LEFT_HAND"
	}

	CheckBox {
		id: force_show_right_hand_cb
		text: "Right Hand"
		property var flagValue: "FORCE_SHOW_RIGHT_HAND"
	}

	CheckBox {
		id: force_show_body_cb
		text: "Body"
		property var flagValue: "FORCE_SHOW_BODY"
	}

      }
    }


    GridLayout {
        id: flagsGridLayout
	columns: 4

	CheckBox {
		id: unique_cb
		text: "Unique"
		property var flagValue: "IS_UNIQUE"
	}

	CheckBox {
		id: always_loot_cb
		text: "Always Loot"
		property var flagValue: "ALWAYS_LOOT"
	}

	CheckBox {
		id: no_parry_cb
		text: "No Parry"
		property var flagValue: "NO_PARRY"
	}

        CheckBox {
                id: default_ammo
                text: "Default Ammo"
		property var flagValue: "IS_DEFAULT_AMMO"
        }

        CheckBox {
                id: merchandise_cb
                text: "Merchandise"
		property var flagValue: "IS_MERCHANDISE"
        }

        CheckBox {
                id: wooden_attack_cb
                text: "Wooden Attack"
		property var flagValue: "WOODEN_ATTACK"
        }

        CheckBox {
                id: wooden_parry_cb
                text: "Wooden Parry"
		property var flagValue: "WOODEN_PARRY"
        }

        CheckBox {
                id: food_cb
                text: "Food"
		property var flagValue: "IS_FOOD"
        }

        CheckBox {
                id: cant_reload_on_horseback_cb
                text: "Cant Reload On Horseback"
		property var flagValue: "IS_CANT_RELOAD_ON_HORSEBACK"
        }

        CheckBox {
                id: two_handed_cb
                text: "Two Handed"
		property var flagValue: "IS_TWO_HANDED"
        }

        CheckBox {
                id: primary_cb
                text: "Primary"
		property var flagValue: "IS_PRIMARY"
        }

        CheckBox {
                id: secondary_cb
                text: "Secondary"
		property var flagValue: "IS_SECONDARY"
        }

        CheckBox {
                id: covers_legs_cb
                text: "Covers Legs"
		property var flagValue: "COVERS_LEGS"
        }

        CheckBox {
                id: civilian_cb
                text: "Civilian"
		property var flagValue: "IS_CIVILIAN"
        }

        CheckBox {
                id: doesnt_cover_hair_cb
                text: "Doesnt Cover Hair"
		property var flagValue: "DOESNT_COVER_HAIR"
        }

        CheckBox {
                id: can_penetrate_shield_cb
                text: "Can Penetrate Shield"
		property var flagValue: "CAN_PENETRATE_SHIELD"
        }

        CheckBox {
                id: consumable_cb
                text: "Consumable"
		property var flagValue: "IS_CONSUMABLE"
        }

        CheckBox {
                id: bonus_against_shield_cb
                text: "Bonus Against Shield"
		property var flagValue: "HAS_BONUS_AGAINST_SHIELD"
        }

        CheckBox {
                id: penalty_with_shield_cb
                text: "Penalty With Shield"
		property var flagValue: "PENALTY_WITH_SHIELD"
        }

        CheckBox {
                id: cant_use_on_horseback_cb
                text: "Cant Use On Horseback"
		property var flagValue: "CANT_USE_ON_HORSEBACK"
        }

        CheckBox {
                id: next_item_as_melee_cb
                text: "Next Item As Melee"
		property var flagValue: "NEXT_ITEM_AS_MELEE"
        }

        CheckBox {
                id: fit_to_head_cb
                text: "Fit To Head"
		property var flagValue: "FIT_TO_HEAD"
        }

        CheckBox {
                id: offset_lance_cb
                text: "Offset Lance"
		property var flagValue: "OFFSET_LANCE"
        }

        CheckBox {
                id: covers_head_cb
                text: "Covers Head"
		property var flagValue: "COVERS_HEAD"
        }

        CheckBox {
                id: couchable_cb
                text: "Couchable"
		property var flagValue: "IS_COUCHABLE"
        }

        CheckBox {
                id: crush_through_cb
                text: "Crush Through"
		property var flagValue: "HAS_CRUSH_THROUGH"
        }

        CheckBox {
                id: knock_back_cb
                text: "Knock Back"
		property var flagValue: "HAS_KNOCK_BACK"
        }

        CheckBox {
                id: remove_item_on_use_cb
                text: "Remove Item On Use"
		property var flagValue: "REMOVE_ITEM_ON_USE"
        }

        CheckBox {
                id: unbalanced_cb
                text: "Unbalanced"
		property var flagValue: "IS_UNBALANCED"
        }

        CheckBox {
                id: covers_beard_cb
                text: "Covers Beard"
		property var flagValue: "COVERS_BEARD"
        }

        CheckBox {
                id: has_bayonet_cb
                text: "Has Bayonet"
		property var flagValue: "HAS_BAYONET"
        }

        CheckBox {
                id: no_pickup_from_ground_cb
                text: "No Pickup From Ground"
		property var flagValue: "NO_PICKUP_FROM_GROUND"
        }

        CheckBox {
                id: can_knock_back_cb
                text: "Can Knock Back"
		property var flagValue: "CAN_KNOCK_BACK"
        }

        CheckBox {
                id: covers_hair_cb
                text: "Covers Hair"
		property var flagValue: "COVERS_HAIR"
        }

        CheckBox {
                id: covers_hair_partially_cb
                text: "Covers Hair Partially"
		property var flagValue: "COVERS_HAIR_PARTIALLY"
        }

        CheckBox {
                id: extra_penetration_cb
                text: "Extra Penetration"
		property var flagValue: "HAS_EXTRA_PENETRATION"
        }

        CheckBox {
                id: no_blur_cb
                text: "No Blur"
		property var flagValue: "HAS_NO_BLUR"
        }

        CheckBox {
                id: cant_reload_while_moving_cb
                text: "Cant Reload While Moving"
		property var flagValue: "CANT_RELOAD_WHILE_MOVING"
        }

	CheckBox {
		id: ignore_gravity_cb
		text: "Ignore Gravity"
		property var flagValue: "IGNORE_GRAVITY"
	}

	CheckBox {
		id: ignore_friction_cb
		text: "Ignore Friction"
		property var flagValue: "IGNORE_FRICTION"
	}

	CheckBox {
		id: is_pike_cb
		text: "Is Pike"
		property var flagValue: "IS_PIKE"
	}

	CheckBox {
		id: offset_musket_cb
		text: "Offset Musket"
		property var flagValue: "OFFSET_MUSKET"
	}

	CheckBox {
		id: cant_reload_while_moving_mounted_cb
		text: "Cant Reload While Moving Mounted"
		property var flagValue: "CANT_RELOAD_WHILE_MOVING_MOUNTED"
	}

	CheckBox {
		id: has_upper_stab_cb
		text: "Has Upper Stab"
		property var flagValue: "HAS_UPPER_STAB"
	}

	CheckBox {
		id: disable_agent_sounds_cb
		text: "Disable Agent Sounds"
		property var flagValue: "DISABLE_AGENT_SOUNDS"
	}

    }
  }
 }

 GroupBox {
   id: capability_flags_gb
	
   ColumnLayout {
   
	GroupBox {
	    	GridLayout {
			Button {
				text: "Test1"
			}
			Button {
				text: "Test2"
			}
		}
	}	

   }
 }
}
