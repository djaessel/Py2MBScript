import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts


ColumnLayout {
    id: itemManagerRoot
    spacing: 0

    property var curItem: null

    function preparePropertyFlags() {
        for (var kchild in flagsGridLayout.children) {
            flagsGridLayout.children[kchild].checked = false
        }

        for (kchild in force_show_row.children) {
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
            for (kchild in flagsGridLayout.children) {
                var checkx = "itp_" + flagsGridLayout.children[kchild].text.replace(' ', '_').toLowerCase()
                if (checkx == flag) {
                    flagsGridLayout.children[kchild].checked = true
                }
            }

            for (kchild in force_show_row.children) {
                checkx = "itp_" + force_show_row.children[kchild].text.replace(' ', '_').toLowerCase()
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

    function removeCapability(name) {
        while (curItem.capabilities.includes(name)) {
            let index = curItem.capabilities.indexOf(name);
            if (index > -1) {
                curItem.capabilities.splice(index, 1);
            }
        }
    }

    function addIfNotIncluded(name) {
        if (!curItem.capabilities.includes(name)) {
            curItem.capabilities.push(name)
        }
    }

    function prepareCapabilityFlags() {
        if (curItem.capabilities.includes("itc_musket_melee")) {
            removeCapability("itc_musket_melee")

            addIfNotIncluded("itc_parry_polearm")
            addIfNotIncluded("itcf_overswing_musket")
            addIfNotIncluded("itcf_thrust_musket")
            addIfNotIncluded("itcf_slashright_twohanded")
            addIfNotIncluded("itcf_slashleft_twohanded")
        }

        if (curItem.capabilities.includes("itc_greatlance")) {
            removeCapability("itc_greatlance")

            addIfNotIncluded("itcf_thrust_onehanded_lance")
            addIfNotIncluded("itcf_thrust_onehanded_lance_horseback")
            addIfNotIncluded("itcf_thrust_polearm")
        }

        if (curItem.capabilities.includes("itc_guandao")) {
            removeCapability("itc_guandao")

            addIfNotIncluded("itc_parry_polearm")
            addIfNotIncluded("itcf_overswing_polearm")
            addIfNotIncluded("itcf_thrust_polearm")
            addIfNotIncluded("itcf_slashright_polearm")
            addIfNotIncluded("itcf_slashleft_polearm")
            addIfNotIncluded("itcf_horseback_slashright_onehanded")
            addIfNotIncluded("itcf_horseback_slashleft_onehanded")
            addIfNotIncluded("itcf_horseback_slash_polearm")
        }

        if (curItem.capabilities.includes("itc_pike")) {
            removeCapability("itc_pike")

            addIfNotIncluded("itcf_thrust_onehanded_lance")
            addIfNotIncluded("itcf_thrust_onehanded_lance_horseback")
            addIfNotIncluded("itcf_thrust_polearm")
        }

        if (curItem.capabilities.includes("itc_cutting_spear")) {
            removeCapability("itc_cutting_spear")

            addIfNotIncluded("itc_spear")
            addIfNotIncluded("itcf_overswing_polearm")
        }

        if (curItem.capabilities.includes("itc_spear")) {
            removeCapability("itc_spear")

            addIfNotIncluded("itc_parry_polearm")
            addIfNotIncluded("itcf_thrust_onehanded_lance")
            addIfNotIncluded("itcf_thrust_onehanded_lance_horseback")
            addIfNotIncluded("itcf_thrust_polearm")
        }

        if (curItem.capabilities.includes("itc_staff")) {
            removeCapability("itc_staff")

            addIfNotIncluded("itc_parry_polearm")
            addIfNotIncluded("itcf_thrust_onehanded_lance")
            addIfNotIncluded("itcf_thrust_onehanded_lance_horseback")
            addIfNotIncluded("itcf_overswing_polearm")
            addIfNotIncluded("itcf_thrust_polearm")
            addIfNotIncluded("itcf_slashright_polearm")
            addIfNotIncluded("itcf_slashleft_polearm")
        }

        if (curItem.capabilities.includes("itc_poleaxe")) {
            removeCapability("itc_poleaxe")

            addIfNotIncluded("itc_parry_polearm")
            addIfNotIncluded("itcf_overswing_polearm")
            addIfNotIncluded("itcf_thrust_polearm")
            addIfNotIncluded("itcf_slashright_polearm")
            addIfNotIncluded("itcf_slashleft_polearm")
        }

        if (curItem.capabilities.includes("itc_parry_polearm")) {
            removeCapability("itc_parry_polearm")

            addIfNotIncluded("itcf_parry_forward_polearm")
            addIfNotIncluded("itcf_parry_up_polearm")
            addIfNotIncluded("itcf_parry_right_polearm")
            addIfNotIncluded("itcf_parry_left_polearm")
        }

        if (curItem.capabilities.includes("itc_morningstar")) {
            removeCapability("itc_morningstar")

            addIfNotIncluded("itc_cut_two_handed")
            addIfNotIncluded("itc_parry_two_handed")
            addIfNotIncluded("itc_cleaver")
        }

        if (curItem.capabilities.includes("itc_bastardsword")) {
            removeCapability("itc_bastardsword")

            addIfNotIncluded("itc_cut_two_handed")
            addIfNotIncluded("itcf_thrust_twohanded")
            addIfNotIncluded("itc_parry_two_handed")
            addIfNotIncluded("itc_dagger")
        }

        if (curItem.capabilities.includes("itc_nodachi")) {
            removeCapability("itc_nodachi")

            addIfNotIncluded("itc_cut_two_handed")
            addIfNotIncluded("itc_parry_two_handed")
        }

        if (curItem.capabilities.includes("itc_greatsword")) {
            removeCapability("itc_greatsword")

            addIfNotIncluded("itc_cut_two_handed")
            addIfNotIncluded("itcf_thrust_twohanded")
            addIfNotIncluded("itc_parry_two_handed")
            addIfNotIncluded("itcf_thrust_onehanded_lance")
        }

        if (curItem.capabilities.includes("itc_cut_two_handed")) {
            removeCapability("itc_cut_two_handed")

            addIfNotIncluded("itcf_force_64_bits")
            addIfNotIncluded("itcf_slashright_twohanded")
            addIfNotIncluded("itcf_slashleft_twohanded")
            addIfNotIncluded("itcf_overswing_twohanded")
            addIfNotIncluded("itcf_horseback_slashright_onehanded")
            addIfNotIncluded("itcf_horseback_slashleft_onehanded")
        }

        if (curItem.capabilities.includes("itc_parry_two_handed")) {
            removeCapability("itc_parry_two_handed")

            addIfNotIncluded("itcf_force_64_bits")
            addIfNotIncluded("itcf_parry_forward_twohanded")
            addIfNotIncluded("itcf_parry_up_twohanded")
            addIfNotIncluded("itcf_parry_right_twohanded")
            addIfNotIncluded("itcf_parry_left_twohanded")
        }

        if (curItem.capabilities.includes("itc_scimitar")) {
            removeCapability("itc_scimitar")

            addIfNotIncluded("itc_cleaver")
            addIfNotIncluded("itc_parry_onehanded")
        }

        if (curItem.capabilities.includes("itc_longsword")) {
            removeCapability("itc_longsword")

            addIfNotIncluded("itc_dagger")
            addIfNotIncluded("itc_parry_onehanded")
        }

        if (curItem.capabilities.includes("itc_parry_onehanded")) {
            removeCapability("itc_parry_onehanded")

            addIfNotIncluded("itcf_force_64_bits")
            addIfNotIncluded("itcf_parry_forward_onehanded")
            addIfNotIncluded("itcf_parry_up_onehanded")
            addIfNotIncluded("itcf_parry_right_onehanded")
            addIfNotIncluded("itcf_parry_left_onehanded")
        }

        if (curItem.capabilities.includes("itc_dagger")) {
            removeCapability("itc_dagger")

            addIfNotIncluded("itc_cleaver")
            addIfNotIncluded("itcf_thrust_onehanded")
        }

        if (curItem.capabilities.includes("itc_cleaver")) {
            removeCapability("itc_cleaver")

            addIfNotIncluded("itcf_force_64_bits")
            addIfNotIncluded("itcf_overswing_onehanded")
            addIfNotIncluded("itcf_slashright_onehanded")
            addIfNotIncluded("itcf_slashleft_onehanded")
            addIfNotIncluded("itcf_horseback_slashright_onehanded")
            addIfNotIncluded("itcf_horseback_slashleft_onehanded")
        }

        //---

        for (var k in onehanded1.children) {
            if (curItem.capabilities.includes(onehanded1.children[k].flagRValue)) {
                onehanded1.children[k].checked = true
            }
        }
        for (k in onehanded2.children) {
            if (curItem.capabilities.includes(onehanded2.children[k].flagRValue)) {
                onehanded2.children[k].checked = true
            }
        }
        for (k in onehanded_horseback.children) {
            if (curItem.capabilities.includes(onehanded_horseback.children[k].flagRValue)) {
                onehanded_horseback.children[k].checked = true
            }
        }
        for (k in onehanded_parry.children) {
            if (curItem.capabilities.includes(onehanded_parry.children[k].flagRValue)) {
                onehanded_parry.children[k].checked = true
            }
        }

        for (k in twohanded.children) {
            if (curItem.capabilities.includes(twohanded.children[k].flagRValue)) {
                twohanded.children[k].checked = true
            }
        }
        for (k in twohanded_parry.children) {
            if (curItem.capabilities.includes(twohanded_parry.children[k].flagRValue)) {
                twohanded_parry.children[k].checked = true
            }
        }

        for (k in polearm.children) {
            if (curItem.capabilities.includes(polearm.children[k].flagRValue)) {
                polearm.children[k].checked = true
            }
        }
        for (k in polearm_parry.children) {
            if (curItem.capabilities.includes(polearm_parry.children[k].flagRValue)) {
                polearm_parry.children[k].checked = true
            }
        }

        for (k in radioGroup.buttons) {
            if (curItem.capabilities.includes(radioGroup.buttons[k].flagRValue)) {
                radioGroup.buttons[k].checked = true
            }
        }

        for (k in throwx.children) {
            if (curItem.capabilities.includes(throwx.children[k].flagRValue)) {
                throwx.children[k].checked = true
            }
        }

        for (k in shoot.children) {
            if (curItem.capabilities.includes(shoot.children[k].flagRValue)) {
                shoot.children[k].checked = true
            }
        }

        for (k in musket.children) {
            if (curItem.capabilities.includes(musket.children[k].flagRValue)) {
                musket.children[k].checked = true
            }
        }

        for (k in others.children) {
            if (curItem.capabilities.includes(others.children[k].flagRValue)) {
                others.children[k].checked = true
            }
        }
    }

    function prepareMeshes() {
    }

    onCurItemChanged: {
        preparePropertyFlags()
        prepareCapabilityFlags()
        prepareMeshes()
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
                meshes_gb.visible = false
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
                meshes_gb.visible = false
            }
        }
        Button {
            id: meshesBtn
            flat: true
            palette.buttonText: "black"
            palette.button: "darkgrey"
            background: Rectangle {
                implicitWidth: 100
                implicitHeight: 25
                border.width: meshesBtn.activeFocus ? 3 : 2
                border.color: "black"
                radius: 2
                gradient: Gradient {
                    GradientStop { position: 0 ; color: meshesBtn.pressed ? "#ccc" : "#eee" }
                    GradientStop { position: 1 ; color: meshesBtn.pressed ? "#aaa" : "#ccc" }
                }
            }

            text: "Meshes"
            onClicked: {
                for (var kchild in tabxs.children) {
                    tabxs.children[kchild].enabled = true
                }
                meshesBtn.enabled = false
                property_flags_gb.visible = false
                capability_flags_gb.visible = false
                meshes_gb.visible = true
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

                for (kchild in flagsGridLayout.children) {
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
                        property string flagValue: "FORCE_SHOW_LEFT_HAND"
                    }

                    CheckBox {
                        id: force_show_right_hand_cb
                        text: "Right Hand"
                        property string flagValue: "FORCE_SHOW_RIGHT_HAND"
                    }

                    CheckBox {
                        id: force_show_body_cb
                        text: "Body"
                        property string flagValue: "FORCE_SHOW_BODY"
                    }

                }
            }


            GridLayout {
                id: flagsGridLayout
                columns: 4

                CheckBox {
                    id: unique_cb
                    text: "Unique"
                    property string flagValue: "IS_UNIQUE"
                }

                CheckBox {
                    id: always_loot_cb
                    text: "Always Loot"
                    property string flagValue: "ALWAYS_LOOT"
                }

                CheckBox {
                    id: no_parry_cb
                    text: "No Parry"
                    property string flagValue: "NO_PARRY"
                }

                CheckBox {
                    id: default_ammo
                    text: "Default Ammo"
                    property string flagValue: "IS_DEFAULT_AMMO"
                }

                CheckBox {
                    id: merchandise_cb
                    text: "Merchandise"
                    property string flagValue: "IS_MERCHANDISE"
                }

                CheckBox {
                    id: wooden_attack_cb
                    text: "Wooden Attack"
                    property string flagValue: "WOODEN_ATTACK"
                }

                CheckBox {
                    id: wooden_parry_cb
                    text: "Wooden Parry"
                    property string flagValue: "WOODEN_PARRY"
                }

                CheckBox {
                    id: food_cb
                    text: "Food"
                    property string flagValue: "IS_FOOD"
                }

                CheckBox {
                    id: cant_reload_on_horseback_cb
                    text: "Cant Reload On Horseback"
                    property string flagValue: "IS_CANT_RELOAD_ON_HORSEBACK"
                }

                CheckBox {
                    id: two_handed_cb
                    text: "Two Handed"
                    property string flagValue: "IS_TWO_HANDED"
                }

                CheckBox {
                    id: primary_cb
                    text: "Primary"
                    property string flagValue: "IS_PRIMARY"
                }

                CheckBox {
                    id: secondary_cb
                    text: "Secondary"
                    property string flagValue: "IS_SECONDARY"
                }

                CheckBox {
                    id: covers_legs_cb
                    text: "Covers Legs"
                    property string flagValue: "COVERS_LEGS"
                }

                CheckBox {
                    id: civilian_cb
                    text: "Civilian"
                    property string flagValue: "IS_CIVILIAN"
                }

                CheckBox {
                    id: doesnt_cover_hair_cb
                    text: "Doesnt Cover Hair"
                    property string flagValue: "DOESNT_COVER_HAIR"
                }

                CheckBox {
                    id: can_penetrate_shield_cb
                    text: "Can Penetrate Shield"
                    property string flagValue: "CAN_PENETRATE_SHIELD"
                }

                CheckBox {
                    id: consumable_cb
                    text: "Consumable"
                    property string flagValue: "IS_CONSUMABLE"
                }

                CheckBox {
                    id: bonus_against_shield_cb
                    text: "Bonus Against Shield"
                    property string flagValue: "HAS_BONUS_AGAINST_SHIELD"
                }

                CheckBox {
                    id: penalty_with_shield_cb
                    text: "Penalty With Shield"
                    property string flagValue: "PENALTY_WITH_SHIELD"
                }

                CheckBox {
                    id: cant_use_on_horseback_cb
                    text: "Cant Use On Horseback"
                    property string flagValue: "CANT_USE_ON_HORSEBACK"
                }

                CheckBox {
                    id: next_item_as_melee_cb
                    text: "Next Item As Melee"
                    property string flagValue: "NEXT_ITEM_AS_MELEE"
                }

                CheckBox {
                    id: fit_to_head_cb
                    text: "Fit To Head"
                    property string flagValue: "FIT_TO_HEAD"
                }

                CheckBox {
                    id: offset_lance_cb
                    text: "Offset Lance"
                    property string flagValue: "OFFSET_LANCE"
                }

                CheckBox {
                    id: covers_head_cb
                    text: "Covers Head"
                    property string flagValue: "COVERS_HEAD"
                }

                CheckBox {
                    id: couchable_cb
                    text: "Couchable"
                    property string flagValue: "IS_COUCHABLE"
                }

                CheckBox {
                    id: crush_through_cb
                    text: "Crush Through"
                    property string flagValue: "HAS_CRUSH_THROUGH"
                }

                CheckBox {
                    id: knock_back_cb
                    text: "Knock Back"
                    property string flagValue: "HAS_KNOCK_BACK"
                }

                CheckBox {
                    id: remove_item_on_use_cb
                    text: "Remove Item On Use"
                    property string flagValue: "REMOVE_ITEM_ON_USE"
                }

                CheckBox {
                    id: unbalanced_cb
                    text: "Unbalanced"
                    property string flagValue: "IS_UNBALANCED"
                }

                CheckBox {
                    id: covers_beard_cb
                    text: "Covers Beard"
                    property string flagValue: "COVERS_BEARD"
                }

                CheckBox {
                    id: has_bayonet_cb
                    text: "Has Bayonet"
                    property string flagValue: "HAS_BAYONET"
                }

                CheckBox {
                    id: no_pickup_from_ground_cb
                    text: "No Pickup From Ground"
                    property string flagValue: "NO_PICKUP_FROM_GROUND"
                }

                CheckBox {
                    id: can_knock_back_cb
                    text: "Can Knock Back"
                    property string flagValue: "CAN_KNOCK_BACK"
                }

                CheckBox {
                    id: covers_hair_cb
                    text: "Covers Hair"
                    property string flagValue: "COVERS_HAIR"
                }

                CheckBox {
                    id: covers_hair_partially_cb
                    text: "Covers Hair Partially"
                    property string flagValue: "COVERS_HAIR_PARTIALLY"
                }

                CheckBox {
                    id: extra_penetration_cb
                    text: "Extra Penetration"
                    property string flagValue: "HAS_EXTRA_PENETRATION"
                }

                CheckBox {
                    id: no_blur_cb
                    text: "No Blur"
                    property string flagValue: "HAS_NO_BLUR"
                }

                CheckBox {
                    id: cant_reload_while_moving_cb
                    text: "Cant Reload While Moving"
                    property string flagValue: "CANT_RELOAD_WHILE_MOVING"
                }

                CheckBox {
                    id: ignore_gravity_cb
                    text: "Ignore Gravity"
                    property string flagValue: "IGNORE_GRAVITY"
                }

                CheckBox {
                    id: ignore_friction_cb
                    text: "Ignore Friction"
                    property string flagValue: "IGNORE_FRICTION"
                }

                CheckBox {
                    id: is_pike_cb
                    text: "Is Pike"
                    property string flagValue: "IS_PIKE"
                }

                CheckBox {
                    id: offset_musket_cb
                    text: "Offset Musket"
                    property string flagValue: "OFFSET_MUSKET"
                }

                CheckBox {
                    id: cant_reload_while_moving_mounted_cb
                    text: "Cant Reload While Moving Mounted"
                    property string flagValue: "CANT_RELOAD_WHILE_MOVING_MOUNTED"
                }

                CheckBox {
                    id: has_upper_stab_cb
                    text: "Has Upper Stab"
                    property string flagValue: "HAS_UPPER_STAB"
                }

                CheckBox {
                    id: disable_agent_sounds_cb
                    text: "Disable Agent Sounds"
                    property string flagValue: "DISABLE_AGENT_SOUNDS"
                }

            }
        }
    }

    GroupBox {
        id: capability_flags_gb

        ColumnLayout {

            GridLayout {
                columns: 2
                GroupBox {
                    title: "Onehanded"
                    ColumnLayout {
                        RowLayout {
                            id: onehanded1
                            CheckBox {
                                text: "Thrust"
                                property string flagValue: "ONEHANDED_TRUST"
                                property string flagRValue: "itcf_thrust_onehanded"
                            }
                            CheckBox {
                                text: "Overswing"
                                property string flagValue: "ONEHANDED_OVERSWING"
                                property string flagRValue: "itcf_overswing_onehanded"
                            }
                            CheckBox {
                                text: "Slashright"
                                property string flagValue: "ONEHANDED_SLASHRIGHT"
                                property string flagRValue: "itcf_slashright_onehanded"
                            }
                            CheckBox {
                                text: "Slashleft"
                                property string flagValue: "ONEHANDED_SLASHLEFT"
                                property string flagRValue: "itcf_slashleft_onehanded"
                            }
                        }
                        RowLayout {
                            id: onehanded2
                            CheckBox {
                                text: "Thrust Lance"
                                property string flagValue: "ONEHANDED_LANCE_THRUST"
                                property string flagRValue: "itcf_thrust_onehanded_lance"
                            }
                        }
                        RowLayout {
                            GroupBox {
                                title: "Horse Back"
                                GridLayout {
                                    id: onehanded_horseback
                                    columns: 3
                                    CheckBox {
                                        text: "Thrust"
                                        property string flagValue: "HORSEBACK_ONEHANDED_THRUST"
                                        property string flagRValue: "itcf_horseback_thrust_onehanded"
                                    }
                                    CheckBox {
                                        text: "Overswing Left"
                                        property string flagValue: ""
                                        property string flagRValue: ""
                                    }
                                    CheckBox {
                                        text: "Overswing Right"
                                        property string flagValue: ""
                                        property string flagRValue: ""
                                    }
                                    CheckBox {
                                        text: "Slashright"
                                        property string flagValue: ""
                                        property string flagRValue: ""
                                    }
                                    CheckBox {
                                        text: "Slashleft"
                                        property string flagValue: ""
                                        property string flagRValue: ""
                                    }
                                    CheckBox {
                                        text: "Thrust Lance"
                                        property string flagValue: ""
                                        property string flagRValue: ""
                                    }
                                }
                            }
                        }

                        RowLayout {
                            GroupBox {
                                title: "Parry"
                                GridLayout {
                                    id: onehanded_parry
                                    columns: 4
                                    CheckBox {
                                        text: "Forward"
                                        property string flagValue: ""
                                        property string flagRValue: ""
                                    }
                                    CheckBox {
                                        text: "Up"
                                        property string flagValue: ""
                                        property string flagRValue: ""
                                    }
                                    CheckBox {
                                        text: "Right"
                                        property string flagValue: ""
                                        property string flagRValue: ""
                                    }
                                    CheckBox {
                                        text: "Left"
                                        property string flagValue: ""
                                        property string flagRValue: ""
                                    }
                                }
                            }
                        }
                    }
                }

                ColumnLayout {
                    GroupBox {
                        title: "Twohanded"
                        ColumnLayout {
                            RowLayout {
                                id: twohanded
                                CheckBox {
                                    text: "Thrust"
                                    property string flagValue: ""
                                    property string flagRValue: ""
                                }
                                CheckBox {
                                    text: "Overswing"
                                    property string flagValue: ""
                                    property string flagRValue: ""
                                }

                                CheckBox {
                                    text: "Slashright"
                                    property string flagValue: ""
                                    property string flagRValue: ""
                                }
                                CheckBox {
                                    text: "Slashleft"
                                    property string flagValue: ""
                                    property string flagRValue: ""
                                }
                            }

                            RowLayout {
                                GroupBox {
                                    title: "Parry"
                                    GridLayout {
                                        id: twohanded_parry
                                        columns: 4
                                        CheckBox {
                                            text: "Forward"
                                            property string flagValue: ""
                                            property string flagRValue: ""
                                        }
                                        CheckBox {
                                            text: "Up"
                                            property string flagValue: ""
                                            property string flagRValue: ""
                                        }
                                        CheckBox {
                                            text: "Right"
                                            property string flagValue: ""
                                            property string flagRValue: ""
                                        }
                                        CheckBox {
                                            text: "Left"
                                            property string flagValue: ""
                                            property string flagRValue: ""
                                        }
                                    }
                                }
                            }

                        }
                    }

                    GroupBox {
                        title: "Polearm"
                        ColumnLayout {
                            RowLayout {
                                id: polearm
                                CheckBox {
                                    text: "Thrust"
                                    property string flagValue: ""
                                    property string flagRValue: ""
                                }
                                CheckBox {
                                    text: "Overswing"
                                    property string flagValue: ""
                                    property string flagRValue: ""
                                }
                                CheckBox {
                                    text: "Slashright"
                                    property string flagValue: ""
                                    property string flagRValue: ""
                                }
                                CheckBox {
                                    text: "Slashleft"
                                    property string flagValue: ""
                                    property string flagRValue: ""
                                }
                            }

                            RowLayout {
                                GroupBox {
                                    title: "Parry"
                                    GridLayout {
                                        id: polearm_parry
                                        columns: 4
                                        CheckBox {
                                            text: "Forward"
                                            property string flagValue: ""
                                            property string flagRValue: ""
                                        }
                                        CheckBox {
                                            text: "Up"
                                            property string flagValue: ""
                                            property string flagRValue: ""
                                        }
                                        CheckBox {
                                            text: "Right"
                                            property string flagValue: ""
                                            property string flagRValue: ""
                                        }

                                        CheckBox {
                                            text: "Left"
                                            property string flagValue: ""
                                            property string flagRValue: ""
                                        }
                                    }
                                }
                            }

                        }
                    }

                }

                GroupBox {
                    title: "Carry"

                    ButtonGroup { id: radioGroup }

                    ColumnLayout {
                        RowLayout {
                            RadioButton {
                                ButtonGroup.group: radioGroup
                                text: "Sword Left Hip"
                                property string flagValue: ""
                                property string flagRValue: ""
                            }
                            RadioButton {
                                ButtonGroup.group: radioGroup
                                text: "Sword Back"
                                property string flagValue: ""
                                property string flagRValue: ""
                            }
                        }
                        RowLayout {
                            RadioButton {
                                ButtonGroup.group: radioGroup
                                text: "Dagger Fron Left"
                                property string flagValue: ""
                                property string flagRValue: ""
                            }
                            RadioButton {
                                ButtonGroup.group: radioGroup
                                text: "Dagger Fron Right"
                                property string flagValue: ""
                                property string flagRValue: ""
                            }
                        }
                        RowLayout {
                            GroupBox {
                                title: "Quiver"
                                ColumnLayout {
                                    RowLayout {
                                        RadioButton {
                                            ButtonGroup.group: radioGroup
                                            text: "Front Right"
                                            property string flagValue: ""
                                            property string flagRValue: ""
                                        }
                                        RadioButton {
                                            ButtonGroup.group: radioGroup
                                            text: "Back Right"
                                            property string flagValue: ""
                                            property string flagRValue: ""
                                        }
                                    }
                                    RowLayout {
                                        RadioButton {
                                            ButtonGroup.group: radioGroup
                                            text: "Back"
                                            property string flagValue: ""
                                            property string flagRValue: ""
                                        }
                                        RadioButton {
                                            ButtonGroup.group: radioGroup
                                            text: "Right Vertical"
                                            property string flagValue: ""
                                            property string flagRValue: ""
                                        }
                                    }
                                }
                            }
                            ColumnLayout {
                                RadioButton {
                                    ButtonGroup.group: radioGroup
                                    text: "Bow Back"
                                    property string flagValue: ""
                                    property string flagRValue: ""
                                }
                                RadioButton {
                                    ButtonGroup.group: radioGroup
                                    text: "Bowcase Left"
                                    property string flagValue: ""
                                    property string flagRValue: ""
                                }
                                RadioButton {
                                    ButtonGroup.group: radioGroup
                                    text: "Crossbow Back"
                                    property string flagValue: ""
                                    property string flagRValue: ""
                                }
                            }
                        }
                        RowLayout {
                            RadioButton {
                                ButtonGroup.group: radioGroup
                                text: "Revolver Right"
                                property string flagValue: ""
                                property string flagRValue: ""
                            }
                            RadioButton {
                                ButtonGroup.group: radioGroup
                                text: "Pistol Front Left"
                                property string flagValue: ""
                                property string flagRValue: ""
                            }
                            RadioButton {
                                ButtonGroup.group: radioGroup
                                text: "Spear"
                                property string flagValue: ""
                                property string flagRValue: ""
                            }
                        }
                        RowLayout {
                            RadioButton {
                                ButtonGroup.group: radioGroup
                                text: "Axe Back"
                                property string flagValue: ""
                                property string flagRValue: ""
                            }
                            RadioButton {
                                ButtonGroup.group: radioGroup
                                text: "Axe Left Hip"
                                property string flagValue: ""
                                property string flagRValue: ""
                            }
                            RadioButton {
                                ButtonGroup.group: radioGroup
                                text: "Mace Left Hip"
                                property string flagValue: ""
                                property string flagRValue: ""
                            }
                        }
                        RowLayout {
                            RadioButton {
                                ButtonGroup.group: radioGroup
                                text: "Kite Shield"
                                property string flagValue: ""
                                property string flagRValue: ""
                            }
                            RadioButton {
                                ButtonGroup.group: radioGroup
                                text: "Round Shield"
                                property string flagValue: ""
                                property string flagRValue: ""
                            }
                            RadioButton {
                                ButtonGroup.group: radioGroup
                                text: "Board Shield"
                                property string flagValue: ""
                                property string flagRValue: ""
                            }
                        }
                        RowLayout {
                            RadioButton {
                                ButtonGroup.group: radioGroup
                                text: "Buckler Left"
                                property string flagValue: ""
                                property string flagRValue: ""
                            }
                            RadioButton {
                                ButtonGroup.group: radioGroup
                                text: "Katana"
                                property string flagValue: ""
                                property string flagRValue: ""
                            }
                            RadioButton {
                                ButtonGroup.group: radioGroup
                                text: "Wakizashi"
                                property string flagValue: ""
                                property string flagRValue: ""
                            }
                        }

                    }
                } // Carry GroupBox

                ColumnLayout {

                    GroupBox {
                        title: "Throw"
                        RowLayout {
                            id: throwx
                            RadioButton {
                                text: "Knife"
                                property string flagValue: ""
                                property string flagRValue: ""
                            }
                            RadioButton {
                                text: "Stone"
                                property string flagValue: ""
                                property string flagRValue: ""
                            }
                            RadioButton {
                                text: "Javelin"
                                property string flagValue: ""
                                property string flagRValue: ""
                            }
                            RadioButton {
                                text: "Axe"
                                property string flagValue: ""
                                property string flagRValue: ""
                            }
                        }
                    }

                    GroupBox {
                        title: "Shoot"
                        RowLayout {
                            id: shoot
                            RadioButton {
                                text: "Bow"
                                property string flagValue: ""
                                property string flagRValue: ""
                            }
                            RadioButton {
                                text: "Crossbow"
                                property string flagValue: ""
                                property string flagRValue: ""
                            }
                            RadioButton {
                                text: "Javelin"
                                property string flagValue: ""
                                property string flagRValue: ""
                            }
                            RadioButton {
                                text: "Pistol"
                                property string flagValue: ""
                                property string flagRValue: ""
                            }
                            RadioButton {
                                text: "Musket"
                                property string flagValue: ""
                                property string flagRValue: ""
                            }
                        }
                    }

                    GroupBox {
                        title: "Musket"
                        RowLayout {
                            id: musket
                            CheckBox {
                                text: "Thrust"
                                property string flagValue: ""
                                property string flagRValue: ""
                            }
                            CheckBox {
                                text: "Overswing"
                                property string flagValue: ""
                                property string flagRValue: ""
                            }
                            CheckBox {
                                text: "Reload"
                                property string flagValue: ""
                                property string flagRValue: ""
                            }
                        }
                    }

                    GroupBox {
                        title: "Others"
                        GridLayout {
                            id: others
                            columns: 2
                            CheckBox {
                                text: "Show Holster When Drawn"
                                property string flagValue: ""
                                property string flagRValue: ""
                            }
                            CheckBox {
                                text: "Reload Pistol"
                                property string flagValue: ""
                                property string flagRValue: ""
                            }
                            CheckBox {
                                text: "Overswing Spear"
                                property string flagValue: ""
                                property string flagRValue: ""
                            }
                            CheckBox {
                                text: "Force 64 Bit"
                                property string flagValue: ""
                                property string flagRValue: ""
                            }
                        }
                    }

                } // ColumnLayout

            } // GridLayout

        } // ColumnLayout
    } // Capability Flags GroupBox

    GroupBox {
        id: meshes_gb

        ColumnLayout {
            RowLayout {
                spacing: 0
                Label {
                    text: "ID"
                    Layout.minimumWidth: 64
                    horizontalAlignment: Text.AlignHCenter
                    background: Rectangle {
                        border.color: "black"
                        border.width: 2
                        color: "transparent"
                    }
                    color: "black"
                    font.pixelSize: 16
                }
                Label {
                    text: "Resource Mesh"
                    Layout.minimumWidth: 300
                    horizontalAlignment: Text.AlignHCenter
                    background: Rectangle {
                        border.color: "black"
                        border.width: 2
                        color: "transparent"
                    }
                    color: "black"
                    font.pixelSize: 16
                }
                Label {
                    text: "Mesh Kind"
                    Layout.minimumWidth: 200
                    horizontalAlignment: Text.AlignHCenter
                    background: Rectangle {
                        border.color: "black"
                        border.width: 2
                        color: "transparent"
                    }
                    color: "black"
                    font.pixelSize: 16
                }
                Label {
                    text: "Modifier Bits"
                    Layout.minimumWidth: 200
                    horizontalAlignment: Text.AlignHCenter
                    background: Rectangle {
                        border.color: "black"
                        border.width: 2
                        color: "transparent"
                    }
                    color: "black"
                    font.pixelSize: 16
                }
                Label {
                    text: "Show"
                    Layout.minimumWidth: 64
                    horizontalAlignment: Text.AlignHCenter
                    background: Rectangle {
                        border.color: "black"
                        border.width: 2
                        color: "transparent"
                    }
                    color: "black"
                    font.pixelSize: 16
                }
                Label {
                    text: "Delete"
                    Layout.minimumWidth: 64
                    horizontalAlignment: Text.AlignHCenter
                    background: Rectangle {
                        border.color: "black"
                        border.width: 2
                        color: "transparent"
                    }
                    color: "black"
                    font.pixelSize: 16
                }
            }

            ColumnLayout {
                id: meshesLayout
            }
        }
    }

}
