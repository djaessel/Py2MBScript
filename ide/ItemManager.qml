import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts


ColumnLayout {
  id: itemManagerRoot
  spacing: 0

  RowLayout {
        id: tabxs
        spacing: 0
	Button {
                id: propertyFlagsBtn
		text: "Property Flags"
                onClicked: {
                        property_flags_gb.visible = true
			propertyFlagsBtn.enabled = false
			capabilityFlagsBtn.enabled = true
                }
	}
	Button {
		id: capabilityFlagsBtn
		text: "Capability Flags"
		onClicked: {
			property_flags_gb.visible = false
                        propertyFlagsBtn.enabled = true
                        capabilityFlagsBtn.enabled = false
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

	CheckBox {
		id: force_show_left_hand_cb
		text: "Left Hand"
	}

	CheckBox {
		id: force_show_right_hand_cb
		text: "Right Hand"
	}

	CheckBox {
		id: force_show_body_cb
		text: "Body"
	}

      }
    }


    GridLayout {
	columns: 4

	CheckBox {
		id: unique_cb
		text: "Unique"
	}

	CheckBox {
		id: always_loot_cb
		text: "Always Loot"
	}

	CheckBox {
		id: no_parry_cb
		text: "No Parry"
	}

        CheckBox {
                id: default_ammo
                text: "Default Ammo"
        }

        CheckBox {
                id: merchandise_cb
                text: "Merchandise"
        }

        CheckBox {
                id: wooden_attack_cb
                text: "Wooden Attack"
        }

        CheckBox {
                id: wooden_parry_cb
                text: "Wooden Parry"
        }

        CheckBox {
                id: food_cb
                text: "Food"
        }

        CheckBox {
                id: cant_reload_on_horseback_cb
                text: "Cant Reload On Horseback"
        }

        CheckBox {
                id: two_handed_cb
                text: "Two Handed"
        }

        CheckBox {
                id: primary_cb
                text: "Primary"
        }

        CheckBox {
                id: secondary_cb
                text: "Secondary"
        }

        CheckBox {
                id: covers_legs_cb
                text: "Covers Legs"
        }

        CheckBox {
                id: civilian_cb
                text: "Civilian"
        }

        CheckBox {
                id: doesnt_cover_hair_cb
                text: "Doesnt Cover Hair"
        }

        CheckBox {
                id: can_penetrate_shield_cb
                text: "Can Penetrate Shield"
        }

        CheckBox {
                id: consumable_cb
                text: "Consumable"
        }

        CheckBox {
                id: bonus_against_shield_cb
                text: "Bonus Against Shield"
        }

        CheckBox {
                id: penalty_with_shield_cb
                text: "Penalty With Shield"
        }

        CheckBox {
                id: cant_use_on_horseback_cb
                text: "Cant Use On Horseback"
        }

        CheckBox {
                id: next_item_as_melee_cb
                text: "Next Item As Melee"
        }

        CheckBox {
                id: fit_to_head_cb
                text: "Fit To Head"
        }

        CheckBox {
                id: offset_lance_cb
                text: "Offset Lance"
        }

        CheckBox {
                id: covers_head_cb
                text: "Covers Head"
        }

        CheckBox {
                id: couchable_cb
                text: "Couchable"
        }

        CheckBox {
                id: crush_through_cb
                text: "Crush Through"
        }

        CheckBox {
                id: knock_back_cb
                text: "Knock Back"
        }

        CheckBox {
                id: remove_item_on_use_cb
                text: "Remove Item On Use"
        }

        CheckBox {
                id: unbalanced_cb
                text: "Unbalanced"
        }

        CheckBox {
                id: covers_beard_cb
                text: "Covers Beard"
        }

        CheckBox {
                id: has_bayonet_cb
                text: "Has Bayonet"
        }

        CheckBox {
                id: no_pickup_from_ground_cb
                text: "No Pickup From Ground"
        }

        CheckBox {
                id: can_knock_back_cb
                text: "Can Knock Back"
        }

        CheckBox {
                id: covers_hair_cb
                text: "Covers Hair"
        }

        CheckBox {
                id: covers_hair_partially_cb
                text: "Covers Hair Partially"
        }

        CheckBox {
                id: extra_penetration_cb
                text: "Extra Penetration"
        }

        CheckBox {
                id: no_blur_cb
                text: "No Blur"
        }

        CheckBox {
                id: cant_reload_while_moving_cb
                text: "Cant Reload While Moving"
        }

	CheckBox {
		id: ignore_gravity_cb
		text: "Ignore Gravity"
	}

	CheckBox {
		id: ignore_friction_cb
		text: "Ignore Friction"
	}

	CheckBox {
		id: is_pike_cb
		text: "Is Pike"
	}

	CheckBox {
		id: offset_musket_cb
		text: "Offset Musket"
	}

	CheckBox {
		id: cant_reload_while_moving_mounted_cb
		text: "Cant Reload While Moving Mounted"
	}

	CheckBox {
		id: has_upper_stab_cb
		text: "Has Upper Stab"
	}

	CheckBox {
		id: disable_agent_sounds_cb
		text: "Disable Agent Sounds"
	}

    }
  }
 }
}
