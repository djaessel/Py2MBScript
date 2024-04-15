import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15


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
            checkFlag(curItem.flags[kflag])
        }
    }

    function checkFlag(flag) {
        for (var kchild in flagsGridLayout.children) {
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

    function removeCapability(name) {
        let entered = false
        while (curItem.capabilities.includes(name)) {
            let index = curItem.capabilities.indexOf(name);
            if (index > -1) {
                curItem.capabilities.splice(index, 1);
                entered = true
            }
        }
        return entered
    }

    function addIfNotIncluded(name) {
        if (!curItem.capabilities.includes(name)) {
            curItem.capabilities.push(name)
        }
    }

    function containsAndRemoveCapability(name) {
        return removeCapability(name)
    }

    function unfoldCapabilities() {
        if (containsAndRemoveCapability("itc_musket_melee")) {
            addIfNotIncluded("itc_parry_polearm")
            addIfNotIncluded("itcf_overswing_musket")
            addIfNotIncluded("itcf_thrust_musket")
            addIfNotIncluded("itcf_slashright_twohanded")
            addIfNotIncluded("itcf_slashleft_twohanded")
        }

        if (containsAndRemoveCapability("itc_greatlance")) {
            addIfNotIncluded("itcf_thrust_onehanded_lance")
            addIfNotIncluded("itcf_thrust_onehanded_lance_horseback")
            addIfNotIncluded("itcf_thrust_polearm")
        }

        if (containsAndRemoveCapability("itc_guandao")) {
            addIfNotIncluded("itc_parry_polearm")
            addIfNotIncluded("itcf_overswing_polearm")
            addIfNotIncluded("itcf_thrust_polearm")
            addIfNotIncluded("itcf_slashright_polearm")
            addIfNotIncluded("itcf_slashleft_polearm")
            addIfNotIncluded("itcf_horseback_slashright_onehanded")
            addIfNotIncluded("itcf_horseback_slashleft_onehanded")
            addIfNotIncluded("itcf_horseback_slash_polearm")
        }

        if (containsAndRemoveCapability("itc_pike")) {
            addIfNotIncluded("itcf_thrust_onehanded_lance")
            addIfNotIncluded("itcf_thrust_onehanded_lance_horseback")
            addIfNotIncluded("itcf_thrust_polearm")
        }

        if (containsAndRemoveCapability("itc_cutting_spear")) {
            addIfNotIncluded("itc_spear")
            addIfNotIncluded("itcf_overswing_polearm")
        }

        if (containsAndRemoveCapability("itc_spear")) {
            addIfNotIncluded("itc_parry_polearm")
            addIfNotIncluded("itcf_thrust_onehanded_lance")
            addIfNotIncluded("itcf_thrust_onehanded_lance_horseback")
            addIfNotIncluded("itcf_thrust_polearm")
        }

        if (containsAndRemoveCapability("itc_staff")) {
            addIfNotIncluded("itc_parry_polearm")
            addIfNotIncluded("itcf_thrust_onehanded_lance")
            addIfNotIncluded("itcf_thrust_onehanded_lance_horseback")
            addIfNotIncluded("itcf_overswing_polearm")
            addIfNotIncluded("itcf_thrust_polearm")
            addIfNotIncluded("itcf_slashright_polearm")
            addIfNotIncluded("itcf_slashleft_polearm")
        }

        if (containsAndRemoveCapability("itc_poleaxe")) {
            addIfNotIncluded("itc_parry_polearm")
            addIfNotIncluded("itcf_overswing_polearm")
            addIfNotIncluded("itcf_thrust_polearm")
            addIfNotIncluded("itcf_slashright_polearm")
            addIfNotIncluded("itcf_slashleft_polearm")
        }

        if (containsAndRemoveCapability("itc_parry_polearm")) {
            addIfNotIncluded("itcf_parry_forward_polearm")
            addIfNotIncluded("itcf_parry_up_polearm")
            addIfNotIncluded("itcf_parry_right_polearm")
            addIfNotIncluded("itcf_parry_left_polearm")
        }

        if (containsAndRemoveCapability("itc_morningstar")) {
            addIfNotIncluded("itc_cut_two_handed")
            addIfNotIncluded("itc_parry_two_handed")
            addIfNotIncluded("itc_cleaver")
        }

        if (containsAndRemoveCapability("itc_bastardsword")) {
            addIfNotIncluded("itc_cut_two_handed")
            addIfNotIncluded("itcf_thrust_twohanded")
            addIfNotIncluded("itc_parry_two_handed")
            addIfNotIncluded("itc_dagger")
        }

        if (containsAndRemoveCapability("itc_nodachi")) {
            addIfNotIncluded("itc_cut_two_handed")
            addIfNotIncluded("itc_parry_two_handed")
        }

        if (containsAndRemoveCapability("itc_greatsword")) {
            addIfNotIncluded("itc_cut_two_handed")
            addIfNotIncluded("itcf_thrust_twohanded")
            addIfNotIncluded("itc_parry_two_handed")
            addIfNotIncluded("itcf_thrust_onehanded_lance")
        }

        if (containsAndRemoveCapability("itc_cut_two_handed")) {
            addIfNotIncluded("itcf_force_64_bits")
            addIfNotIncluded("itcf_slashright_twohanded")
            addIfNotIncluded("itcf_slashleft_twohanded")
            addIfNotIncluded("itcf_overswing_twohanded")
            addIfNotIncluded("itcf_horseback_slashright_onehanded")
            addIfNotIncluded("itcf_horseback_slashleft_onehanded")
        }

        if (containsAndRemoveCapability("itc_parry_two_handed")) {
            addIfNotIncluded("itcf_force_64_bits")
            addIfNotIncluded("itcf_parry_forward_twohanded")
            addIfNotIncluded("itcf_parry_up_twohanded")
            addIfNotIncluded("itcf_parry_right_twohanded")
            addIfNotIncluded("itcf_parry_left_twohanded")
        }

        if (containsAndRemoveCapability("itc_scimitar")) {
            addIfNotIncluded("itc_cleaver")
            addIfNotIncluded("itc_parry_onehanded")
        }

        if (containsAndRemoveCapability("itc_longsword")) {
            addIfNotIncluded("itc_dagger")
            addIfNotIncluded("itc_parry_onehanded")
        }

        if (containsAndRemoveCapability("itc_parry_onehanded")) {
            addIfNotIncluded("itcf_force_64_bits")
            addIfNotIncluded("itcf_parry_forward_onehanded")
            addIfNotIncluded("itcf_parry_up_onehanded")
            addIfNotIncluded("itcf_parry_right_onehanded")
            addIfNotIncluded("itcf_parry_left_onehanded")
        }

        if (containsAndRemoveCapability("itc_dagger")) {
            addIfNotIncluded("itc_cleaver")
            addIfNotIncluded("itcf_thrust_onehanded")
        }

        if (containsAndRemoveCapability("itc_cleaver")) {
            addIfNotIncluded("itcf_force_64_bits")
            addIfNotIncluded("itcf_overswing_onehanded")
            addIfNotIncluded("itcf_slashright_onehanded")
            addIfNotIncluded("itcf_slashleft_onehanded")
            addIfNotIncluded("itcf_horseback_slashright_onehanded")
            addIfNotIncluded("itcf_horseback_slashleft_onehanded")
        }
    }

    function setCheckedCapabilities() {
        //- onehanded -
        for (var k in onehanded1.children) {
            onehanded1.children[k].checked = false
        }
        for (k in onehanded2.children) {
            onehanded2.children[k].checked = false
        }
        for (k in onehanded_horseback.children) {
            onehanded_horseback.children[k].checked = false
        }
        for (k in onehanded_parry.children) {
            onehanded_parry.children[k].checked = false
        }
        for (k in onehanded1.children) {
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

        //- twohanded -
        for (k in twohanded.children) {
            twohanded.children[k].checked = false
        }
        for (k in twohanded_parry.children) {
            twohanded_parry.children[k].checked = false
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

        //- polearm -
        for (k in polearm.children) {
            polearm.children[k].checked = false
        }
        for (k in polearm_horseback.children) {
            polearm_horseback.children[k].checked = false
        }
        for (k in polearm_parry.children) {
            polearm_parry.children[k].checked = false
        }
        for (k in polearm.children) {
            if (curItem.capabilities.includes(polearm.children[k].flagRValue)) {
                polearm.children[k].checked = true
            }
        }
        for (k in polearm_horseback.children) {
            if (curItem.capabilities.includes(polearm_horseback.children[k].flagRValue)) {
                polearm_horseback.children[k].checked = true
            }
        }
        for (k in polearm_parry.children) {
            if (curItem.capabilities.includes(polearm_parry.children[k].flagRValue)) {
                polearm_parry.children[k].checked = true
            }
        }

        //- carry -
        for (k in radioGroup.buttons) {
            radioGroup.buttons[k].checked = false
        }
        for (k in radioGroup.buttons) {
            if (curItem.capabilities.includes(radioGroup.buttons[k].flagRValue)) {
                radioGroup.buttons[k].checked = true
            }
        }

        //- throw -
        for (k in throwx.children) {
            throwx.children[k].checked = false
        }
        for (k in throwx.children) {
            if (curItem.capabilities.includes(throwx.children[k].flagRValue)) {
                throwx.children[k].checked = true
            }
        }

        //- shoot -
        for (k in shoot.children) {
            shoot.children[k].checked = false
        }
        for (k in shoot.children) {
            if (curItem.capabilities.includes(shoot.children[k].flagRValue)) {
                shoot.children[k].checked = true
            }
        }

        //- musket -
        for (k in musket.children) {
            musket.children[k].checked = false
        }
        for (k in musket.children) {
            if (curItem.capabilities.includes(musket.children[k].flagRValue)) {
                musket.children[k].checked = true
            }
        }

        //- others -
        for (k in others.children) {
            others.children[k].checked = false
        }
        for (k in others.children) {
            if (curItem.capabilities.includes(others.children[k].flagRValue)) {
                others.children[k].checked = true
            }
        }
    }

    function prepareCapabilityFlags() {
        unfoldCapabilities()
        setCheckedCapabilities()
    }

    function createNewMesh(index, resourceName, modifierx, meshKind) {
        var component = Qt.createComponent("MeshX.qml");
        if (component.status == Component.Ready) {
            var meshx = component.createObject(meshesLayout);
            meshx.modifiers = modifierx
            meshx.resourceName = resourceName
            meshx.meshKind = meshKind
            meshx.idText = "" + (index+1)
        }
    }

    function prepareMeshes() {
        for (var i = meshesLayout.children.length - 1; i >= 0; i--) {
            meshesLayout.children[i].destroy()
        }

        for (i = 0; i < curItem.meshes.length; i++) {
            createNewMesh(i, curItem.meshes[i].id, curItem.meshes[i].modifier, 0) // FIXME: add mesh kind to mesh
        }
    }

    /*function resetStats() {
        //priceVal.value = 0

        weightVal.value = 0

        difficultyVal.value = 0
        headArmorVal.value = 0
        bodyArmorVal.value = 0
        legArmorVal.value = 0
        hitPointsVal.value = 0
        speedRatingVal.value = 0
        missileSpeedVal.value = 0
        horseScaleVal.value = 0
        weaponLengthVal.value = 0
        shieldWidthVal.value = 0
        shieldHeightVal.value = 0
        maxAmmoVal.value = 0
        swingDamageVal.value = 0
        swingDamageType.currentIndex = 0
        thrustDamageVal.value = 0
        thrustDamageType.currentIndex = 0
        horseSpeedVal.value = 0
        horseManeuverVal.value = 0
        horseChargeVal.value = 0
        foodQualityVal.value = 0
        abundanceVal.value = 0
        accuracyVal.value = 0
    }*/

    function prepareStats() {
        //resetStats()

        priceVal.value = curItem.price

        weightVal.value = wy(curItem.weight)

        difficultyVal.value = curItem.difficulty
        headArmorVal.value = curItem.head_armor
        bodyArmorVal.value = curItem.body_armor
        legArmorVal.value = curItem.leg_armor
        hitPointsVal.value = curItem.hit_points
        speedRatingVal.value = curItem.speed_rating
        missileSpeedVal.value = curItem.missle_speed
        horseScaleVal.value = curItem.horse_scale
        weaponLengthVal.value = curItem.weapon_length
        shieldWidthVal.value = curItem.shield_width
        shieldHeightVal.value = curItem.shield_height
        maxAmmoVal.value = curItem.max_ammo

        swingDamageVal.value = parseInt(curItem.swing_damage.split(',')[0].replace("(", ""))
        swingDamageType.currentIndex = parseInt(curItem.swing_damage.split(',')[1].replace(")", ""))
        thrustDamageVal.value = parseInt(curItem.thrust_damage.split(',')[0].replace("(", ""))
        thrustDamageType.currentIndex = parseInt(curItem.thrust_damage.split(',')[1].replace(")", ""))

        horseSpeedVal.value = curItem.horse_speed
        horseManeuverVal.value = curItem.horse_maneuver
        horseChargeVal.value = curItem.horse_charge
        foodQualityVal.value = curItem.food_quality
        abundanceVal.value = curItem.abundance
        accuracyVal.value = curItem.accuracy
    }

    onCurItemChanged: {
        preparePropertyFlags()
        prepareCapabilityFlags()
        prepareMeshes()
        prepareStats()
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
                stats_and_price_gb.visible = false
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
                stats_and_price_gb.visible = false
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
                stats_and_price_gb.visible = false
            }
        }
        Button {
            id: statsAndPriceBtn
            flat: true
            palette.buttonText: "black"
            palette.button: "darkgrey"
            background: Rectangle {
                implicitWidth: 100
                implicitHeight: 25
                border.width: statsAndPriceBtn.activeFocus ? 3 : 2
                border.color: "black"
                radius: 2
                gradient: Gradient {
                    GradientStop { position: 0 ; color: statsAndPriceBtn.pressed ? "#ccc" : "#eee" }
                    GradientStop { position: 1 ; color: statsAndPriceBtn.pressed ? "#aaa" : "#ccc" }
                }
            }

            text: "Stats"
            onClicked: {
                for (var kchild in tabxs.children) {
                    tabxs.children[kchild].enabled = true
                }
                statsAndPriceBtn.enabled = false
                property_flags_gb.visible = false
                capability_flags_gb.visible = false
                meshes_gb.visible = false
                stats_and_price_gb.visible = true
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

                xxxxx = saveData(xxxxx, idxs, idxFirst)

                textHandler.setText(xxxxx)
                textArea.text = textHandler.getText()
            }

            function saveItem() {
                let newText = "<p>" + curItem.id + " = Item(\"" + curItem.id + "\", \"" + curItem.name + "\", " + curItem.price + ")</p>"

                newText += saveMeshes()
                newText += savePropertyFlags()
                newText += saveCapabilityFlags()
                newText += saveStats()

                return newText
            }

            function textForSetStat(name, val, val2=-1) {
                let txt = ""
                if (val > 0 && val2 === -1) {
                    txt = "<p>" + curItem.id + ".set_" + name + "(" + val + ")</p>"
                } else if (val > 0 && val2 >= 0) {
                    txt = "<p>" + curItem.id + ".set_" + name + "(" + val + ", " + val2 + ")</p>"
                }

                return txt
            }

            function saveStats() {
                let txt = ""

                var weightx = "" + wx(weightVal.value, null)
                weightx = weightx.trim('0')
                weightx = Number.parseFloat(weightx)

                // TODO: overwrite curItem and use that instead!!!

                txt += textForSetStat("weight", weightx)
                txt += textForSetStat("difficulty", difficultyVal.value)
                txt += textForSetStat("head_armor", headArmorVal.value)
                txt += textForSetStat("body_armor", bodyArmorVal.value)
                txt += textForSetStat("leg_armor", legArmorVal.value)
                txt += textForSetStat("hit_points", hitPointsVal.value)
                txt += textForSetStat("speed_rating", speedRatingVal.value)
                txt += textForSetStat("missle_speed", missileSpeedVal.value)
                txt += textForSetStat("horse_scale", horseScaleVal.value)
                txt += textForSetStat("weapon_length", weaponLengthVal.value)
                txt += textForSetStat("shield_width", shieldWidthVal.value)
                txt += textForSetStat("shield_height", shieldHeightVal.value)
                txt += textForSetStat("max_ammo", maxAmmoVal.value)
                txt += textForSetStat("swing_damage", swingDamageVal.value, swingDamageType.currentIndex)
                txt += textForSetStat("thrust_damage", thrustDamageVal.value, thrustDamageType.currentIndex)
                txt += textForSetStat("horse_speed", horseSpeedVal.value)
                txt += textForSetStat("horse_maneuver", horseManeuverVal.value)
                txt += textForSetStat("horse_charge", horseChargeVal.value)
                txt += textForSetStat("food_quality", foodQualityVal.value)
                txt += textForSetStat("abundance", abundanceVal.value)
                txt += textForSetStat("accuracy", accuracyVal.value)

                return txt
            }

            function saveMeshes() {
                let newText = ""
                for (var kmesh in curItem.meshes) {
                    newText += "<p>" + curItem.id + ".add_mesh(ItemMesh(\"" + curItem.meshes[kmesh].id + "\""
                    if (curItem.meshes[kmesh].modifier != "0") {
                        newText += "," + curItem.meshes[kmesh].modifier
                    }
                    newText += "))</p>"
                }
                return newText
            }

            function savePropertyFlags() {
                let newText = ""

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

                return newText
            }

            function saveCapabilityFlags() {
                var newText = ""

                //- onehanded -
                for (var k in onehanded1.children) {
                    if (onehanded1.children[k].checked) {
                        newText += "<p>" + curItem.id + ".add_capability(ItemCapability." + onehanded1.children[k].flagValue + ")</p>"
                    }
                }
                for (k in onehanded2.children) {
                    if (onehanded2.children[k].checked) {
                        newText += "<p>" + curItem.id + ".add_capability(ItemCapability." + onehanded2.children[k].flagValue + ")</p>"
                    }
                }
                for (k in onehanded_horseback.children) {
                    if (onehanded_horseback.children[k].checked) {
                        newText += "<p>" + curItem.id + ".add_capability(ItemCapability." + onehanded_horseback.children[k].flagValue + ")</p>"
                    }
                }
                for (k in onehanded_parry.children) {
                    if (onehanded_parry.children[k].checked) {
                        newText += "<p>" + curItem.id + ".add_capability(ItemCapability." + onehanded_parry.children[k].flagValue + ")</p>"
                    }
                }

                //- twohanded -
                for (k in twohanded.children) {
                    if (twohanded.children[k].checked) {
                        newText += "<p>" + curItem.id + ".add_capability(ItemCapability." + twohanded.children[k].flagValue + ")</p>"
                    }
                }
                for (k in twohanded_parry.children) {
                    if (twohanded_parry.children[k].checked) {
                        newText += "<p>" + curItem.id + ".add_capability(ItemCapability." + twohanded_parry.children[k].flagValue + ")</p>"
                    }
                }

                //- polearm -
                for (k in polearm.children) {
                    if (polearm.children[k].checked) {
                        newText += "<p>" + curItem.id + ".add_capability(ItemCapability." + polearm.children[k].flagValue + ")</p>"
                    }
                }
                for (k in polearm_horseback.children) {
                    if (polearm_horseback.children[k].checked) {
                        newText += "<p>" + curItem.id + ".add_capability(ItemCapability." + polearm_horseback.children[k].flagValue + ")</p>"
                    }
                }
                for (k in polearm_parry.children) {
                    if (polearm_parry.children[k].checked) {
                        newText += "<p>" + curItem.id + ".add_capability(ItemCapability." + polearm_parry.children[k].flagValue + ")</p>"
                    }
                }

                //- carry -
                for (k in radioGroup.buttons) {
                    if (radioGroup.buttons[k].checked) {
                        newText += "<p>" + curItem.id + ".add_capability(ItemCapability." + radioGroup.buttons[k].flagValue + ")</p>"
                    }
                }

                //- throw -
                for (k in throwx.children) {
                    if (throwx.children[k].checked) {
                        newText += "<p>" + curItem.id + ".add_capability(ItemCapability." + throwx.children[k].flagValue + ")</p>"
                    }
                }

                //- shoot -
                for (k in shoot.children) {
                    if (shoot.children[k].checked) {
                        newText += "<p>" + curItem.id + ".add_capability(ItemCapability." + shoot.children[k].flagValue + ")</p>"
                    }
                }

                //- musket -
                for (k in musket.children) {
                    if (musket.children[k].checked) {
                        newText += "<p>" + curItem.id + ".add_capability(ItemCapability." + musket.children[k].flagValue + ")</p>"
                    }
                }

                //- others -
                for (k in others.children) {
                    if (others.children[k].checked) {
                        newText += "<p>" + curItem.id + ".add_capability(ItemCapability." + others.children[k].flagValue + ")</p>"
                    }
                }

                return newText
            }

            function saveData(xxxxx, idxs, idxFirst) {
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

                // remove altered code parts
                let result = xxxxx.replace("<p></p>", "");
                while (xxxxx != result) {
                    xxxxx = result;
                    result = xxxxx.replace("<p></p>", "");
                }

                let newText = saveItem()

                // idxFirst - 3 --> <p> gets removed!!!
                xxxxx = xxxxx.slice(0, idxFirst - 3) + newText + xxxxx.slice(idxFirst - 3)

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
                                        property string flagValue: "HORSEBACK_ONEHANDED_OVERSWING_LEFT"
                                        property string flagRValue: "itcf_horseback_overswing_left_onehanded"
                                    }
                                    CheckBox {
                                        text: "Overswing Right"
                                        property string flagValue: "HORSEBACK_ONEHANDED_OVERSWING_RIGHT"
                                        property string flagRValue: "itcf_horseback_overswing_right_onehanded"
                                    }
                                    CheckBox {
                                        text: "Slashright"
                                        property string flagValue: "HORSEBACK_ONEHANDED_SLASHRIGHT"
                                        property string flagRValue: "itcf_horseback_slashright_onehanded"
                                    }
                                    CheckBox {
                                        text: "Slashleft"
                                        property string flagValue: "HORSEBACK_ONEHANDED_SLASHLEFT"
                                        property string flagRValue: "itcf_horseback_slashleft_onehanded"
                                    }
                                    CheckBox {
                                        text: "Thrust Lance"
                                        property string flagValue: "HORSEBACK_ONEHANDED_LANCE_THRUST"
                                        property string flagRValue: "itcf_thrust_onehanded_lance_horseback"
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
                                        property string flagValue: "ONEHANDED_PARRY_FORWARD"
                                        property string flagRValue: "itcf_parry_forward_onehanded"
                                    }
                                    CheckBox {
                                        text: "Up"
                                        property string flagValue: "ONEHANDED_PARRY_UP"
                                        property string flagRValue: "itcf_parry_up_onehanded"
                                    }
                                    CheckBox {
                                        text: "Right"
                                        property string flagValue: "ONEHANDED_PARRY_RIGHT"
                                        property string flagRValue: "itcf_parry_right_onehanded"
                                    }
                                    CheckBox {
                                        text: "Left"
                                        property string flagValue: "ONEHANDED_PARRY_LEFT"
                                        property string flagRValue: "itcf_parry_left_onehanded"
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
                                    property string flagValue: "TWOHANDED_THRUST"
                                    property string flagRValue: "itcf_thrust_twohanded"
                                }
                                CheckBox {
                                    text: "Overswing"
                                    property string flagValue: "TWOHANDED_OVERSWING"
                                    property string flagRValue: "itcf_overswing_twohanded"
                                }

                                CheckBox {
                                    text: "Slashright"
                                    property string flagValue: "TWOHANDED_SLASHRIGHT"
                                    property string flagRValue: "itcf_slashright_twohanded"
                                }
                                CheckBox {
                                    text: "Slashleft"
                                    property string flagValue: "TWOHANDED_SLASHLEFT"
                                    property string flagRValue: "itcf_slashleft_twohanded"
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
                                            property string flagValue: "TWOHANDED_PARRY_FORWARD"
                                            property string flagRValue: "itcf_parry_forward_twohanded"
                                        }
                                        CheckBox {
                                            text: "Up"
                                            property string flagValue: "TWOHANDED_PARRY_UP"
                                            property string flagRValue: "itcf_parry_up_twohanded"
                                        }
                                        CheckBox {
                                            text: "Right"
                                            property string flagValue: "TWOHANDED_PARRY_RIGHT"
                                            property string flagRValue: "itcf_parry_right_twohanded"
                                        }
                                        CheckBox {
                                            text: "Left"
                                            property string flagValue: "TWOHANDED_PARRY_LEFT"
                                            property string flagRValue: "itcf_parry_left_twohanded"
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
                                    property string flagValue: "POLEARM_THRUST"
                                    property string flagRValue: "itcf_thrust_polearm"
                                }
                                CheckBox {
                                    text: "Overswing"
                                    property string flagValue: "POLEARM_OVERSWING"
                                    property string flagRValue: "itcf_overswing_polearm"
                                }
                                CheckBox {
                                    text: "Slashright"
                                    property string flagValue: "POLEARM_SLASHRIGHT"
                                    property string flagRValue: "itcf_slashright_polearm"
                                }
                                CheckBox {
                                    text: "Slashleft"
                                    property string flagValue: "POLEARM_SLASHLEFT"
                                    property string flagRValue: "itcf_slashleft_polearm"
                                }
                            }

                            RowLayout {
                                GroupBox {
                                    title: "Horse Back"
                                    GridLayout {
                                        id: polearm_horseback
                                        columns: 3
                                        CheckBox {
                                            text: "Thrust"
                                            property string flagValue: "HORSEBACK_POLEARM_SLASH"
                                            property string flagRValue: "itcf_horseback_slash_polearm"
                                        }
                                    }
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
                                            property string flagValue: "POLEARM_PARRY_FORWARD"
                                            property string flagRValue: "itcf_parry_forward_polearm"
                                        }
                                        CheckBox {
                                            text: "Up"
                                            property string flagValue: "POLEARM_PARRY_UP"
                                            property string flagRValue: "itcf_parry_up_polearm"
                                        }
                                        CheckBox {
                                            text: "Right"
                                            property string flagValue: "POLEARM_PARRY_RIGHT"
                                            property string flagRValue: "itcf_parry_right_polearm"
                                        }

                                        CheckBox {
                                            text: "Left"
                                            property string flagValue: "POLEARM_PARRY_LEFT"
                                            property string flagRValue: "itcf_parry_left_polearm"
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
                                property string flagValue: "CARRY_SWORD_LEFT_HIP"
                                property string flagRValue: "itcf_carry_sword_left_hip"
                            }
                            RadioButton {
                                ButtonGroup.group: radioGroup
                                text: "Sword Back"
                                property string flagValue: "CARRY_SWORD_BACK"
                                property string flagRValue: "itcf_carry_sword_back"
                            }
                        }
                        RowLayout {
                            RadioButton {
                                ButtonGroup.group: radioGroup
                                text: "Dagger Fron Left"
                                property string flagValue: "CARRY_DAGGER_FRONT_LEFT"
                                property string flagRValue: "itcf_carry_dagger_front_left"
                            }
                            RadioButton {
                                ButtonGroup.group: radioGroup
                                text: "Dagger Fron Right"
                                property string flagValue: "CARRY_DAGGER_FRONT_RIGHT"
                                property string flagRValue: "itcf_carry_dagger_front_right"
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
                                            property string flagValue: "CARRY_QUIVER_FRONT_RIGHT"
                                            property string flagRValue: "itcf_carry_quiver_front_right"
                                        }
                                        RadioButton {
                                            ButtonGroup.group: radioGroup
                                            text: "Back Right"
                                            property string flagValue: "CARRY_QUIVER_BACK_RIGHT"
                                            property string flagRValue: "itcf_carry_quiver_back_right"
                                        }
                                    }
                                    RowLayout {
                                        RadioButton {
                                            ButtonGroup.group: radioGroup
                                            text: "Back"
                                            property string flagValue: "CARRY_QUIVER_BACK"
                                            property string flagRValue: "itcf_carry_quiver_back"
                                        }
                                        RadioButton {
                                            ButtonGroup.group: radioGroup
                                            text: "Right Vertical"
                                            property string flagValue: "CARRY_QUIVER_RIGHT_VERTICAL"
                                            property string flagRValue: "itcf_carry_quiver_right_vertical"
                                        }
                                    }
                                }
                            }
                            ColumnLayout {
                                RadioButton {
                                    ButtonGroup.group: radioGroup
                                    text: "Bow Back"
                                    property string flagValue: "CARRY_BOW_BACK"
                                    property string flagRValue: "itcf_carry_bow_back"
                                }
                                RadioButton {
                                    ButtonGroup.group: radioGroup
                                    text: "Bowcase Left"
                                    property string flagValue: "CARRY_BOWCASE_LEFT"
                                    property string flagRValue: "itcf_carry_bowcase_left"
                                }
                                RadioButton {
                                    ButtonGroup.group: radioGroup
                                    text: "Crossbow Back"
                                    property string flagValue: "CARRY_CROSSBOW_BACK"
                                    property string flagRValue: "itcf_carry_crossbow_back"
                                }
                            }
                        }
                        RowLayout {
                            RadioButton {
                                ButtonGroup.group: radioGroup
                                text: "Revolver Right"
                                property string flagValue: "CARRY_REVOLVER_RIGHT"
                                property string flagRValue: "itcf_carry_revolver_right"
                            }
                            RadioButton {
                                ButtonGroup.group: radioGroup
                                text: "Pistol Front Left"
                                property string flagValue: "CARRY_PISTOL_FRONT_LEFT"
                                property string flagRValue: "itcf_carry_pistol_front_left"
                            }
                            RadioButton {
                                ButtonGroup.group: radioGroup
                                text: "Spear"
                                property string flagValue: "CARRY_SPEAR"
                                property string flagRValue: "itcf_carry_spear"
                            }
                        }
                        RowLayout {
                            RadioButton {
                                ButtonGroup.group: radioGroup
                                text: "Axe Back"
                                property string flagValue: "CARRY_AXE_BACK"
                                property string flagRValue: "itcf_carry_axe_back"
                            }
                            RadioButton {
                                ButtonGroup.group: radioGroup
                                text: "Axe Left Hip"
                                property string flagValue: "CARRY_AXE_LEFT_HIP"
                                property string flagRValue: "itcf_carry_axe_left_hip"
                            }
                            RadioButton {
                                ButtonGroup.group: radioGroup
                                text: "Mace Left Hip"
                                property string flagValue: "CARRY_MACE_LEFT_HIP"
                                property string flagRValue: "itcf_carry_mace_left_hip"
                            }
                        }
                        RowLayout {
                            RadioButton {
                                ButtonGroup.group: radioGroup
                                text: "Kite Shield"
                                property string flagValue: "CARRY_KITE_SHIELD"
                                property string flagRValue: "itcf_carry_kite_shield"
                            }
                            RadioButton {
                                ButtonGroup.group: radioGroup
                                text: "Round Shield"
                                property string flagValue: "CARRY_ROUND_SHIELD"
                                property string flagRValue: "itcf_carry_round_shield"
                            }
                            RadioButton {
                                ButtonGroup.group: radioGroup
                                text: "Board Shield"
                                property string flagValue: "CARRY_BOARD_SHIELD"
                                property string flagRValue: "itcf_carry_board_shield"
                            }
                        }
                        RowLayout {
                            RadioButton {
                                ButtonGroup.group: radioGroup
                                text: "Buckler Left"
                                property string flagValue: "CARRY_BUCKLER_LEFT"
                                property string flagRValue: "itcf_carry_buckler_left"
                            }
                            RadioButton {
                                ButtonGroup.group: radioGroup
                                text: "Katana"
                                property string flagValue: "CARRY_KATANA"
                                property string flagRValue: "itcf_carry_katana"
                            }
                            RadioButton {
                                ButtonGroup.group: radioGroup
                                text: "Wakizashi"
                                property string flagValue: "CARRY_WAKIZASHI"
                                property string flagRValue: "itcf_carry_wakizashi"
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
                                property string flagValue: "THROW_KNIFE"
                                property string flagRValue: "itcf_throw_knife"
                            }
                            RadioButton {
                                text: "Stone"
                                property string flagValue: "THROW_STONE"
                                property string flagRValue: "itcf_throw_stone"
                            }
                            RadioButton {
                                text: "Javelin"
                                property string flagValue: "THROW_JAVELIN"
                                property string flagRValue: "itcf_throw_javelin"
                            }
                            RadioButton {
                                text: "Axe"
                                property string flagValue: "THROW_AXE"
                                property string flagRValue: "itcf_throw_axe"
                            }
                        }
                    }

                    GroupBox {
                        title: "Shoot"
                        RowLayout {
                            id: shoot
                            RadioButton {
                                text: "Bow"
                                property string flagValue: "SHOOT_BOW"
                                property string flagRValue: "itcf_shoot_bow"
                            }
                            RadioButton {
                                text: "Crossbow"
                                property string flagValue: "SHOOT_CROSSBOW"
                                property string flagRValue: "itcf_shoot_crossbow"
                            }
                            RadioButton {
                                text: "Javelin"
                                property string flagValue: "SHOOT_JAVELIN"
                                property string flagRValue: "itcf_shoot_javelin"
                            }
                            RadioButton {
                                text: "Pistol"
                                property string flagValue: "SHOOT_PISTOL"
                                property string flagRValue: "itcf_shoot_pistol"
                            }
                            RadioButton {
                                text: "Musket"
                                property string flagValue: "SHOOT_MUSKET"
                                property string flagRValue: "itcf_shoot_musket"
                            }
                        }
                    }

                    GroupBox {
                        title: "Musket"
                        RowLayout {
                            id: musket
                            CheckBox {
                                text: "Thrust"
                                property string flagValue: "MUSTKET_THRUST"
                                property string flagRValue: "itcf_thrust_musket"
                            }
                            CheckBox {
                                text: "Overswing"
                                property string flagValue: "MUSTKET_OVERSWING"
                                property string flagRValue: "itcf_overswing_musket"
                            }
                            CheckBox {
                                text: "Reload"
                                property string flagValue: "RELOAD_MUSTKET"
                                property string flagRValue: "itcf_reload_musket"
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
                                property string flagValue: "SHOW_HOLSTER_WHEN_DRAWN"
                                property string flagRValue: "itcf_show_holster_when_drawn"
                            }
                            CheckBox {
                                text: "Reload Pistol"
                                property string flagValue: "RELOAD_PISTOL"
                                property string flagRValue: "itcf_reload_pistol"
                            }
                            CheckBox {
                                text: "Overswing Spear"
                                property string flagValue: "SPEAR_OVERSWING"
                                property string flagRValue: "itcf_overswing_spear"
                            }
                            CheckBox {
                                text: "Force 64 Bit"
                                property string flagValue: "FORCE_64_BITS"
                                property string flagRValue: "itcf_force_64_bits"
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
                    Layout.minimumWidth: 80
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

            Button {
                id: createNewMeshBtn
                Layout.minimumWidth: parent.width
                flat: true
                text: "+"
                onClicked: {
                    let resName = "<resource_name_" + meshesLayout.children.length + ">"
                    createNewMesh(meshesLayout.children.length, resName, "0", 0)
                    curItem.meshes.push({id: resName, modifier: "0"})
                }
            }
        }
    } // GroupBox Meshes

    function wx(value, locale) {
        let num = Number(value / Math.pow(10, weightVal.decimals))
        return Number.parseFloat(num).toFixed(weightVal.decimals)
    }

    function wy(text, locale) {
        return Number.parseFloat(text) * Math.pow(10, weightVal.decimals)
    }

    GroupBox {
        id: stats_and_price_gb

        onVisibleChanged: {
            if (!stats_and_price_gb.visible) return

            for (var k in stats_and_price_grid.children) {
                stats_and_price_grid.children[k].visible = false
            }

            difficultyCol.visible = true
            weightCol.visible = true
            priceCol.visible = true

            switch (type_cbb.currentIndex) {
            case 1: // horse
            case 18: // animal
                horseChargeCol.visible = true
                horseManeuverCol.visible = true
                horseScaleCol.visible = true
                horseSpeedCol.visible = true
                hitPointsCol.visible = true
                break
            case 2: // one_handed_wpn
            case 3: // two_handed_wpn
            case 4: // polearm
                weaponLengthCol.visible = true
                speedRatingCol.visible = true
                swingDamageCol.visible = true
                thrustDamageCol.visible = true
                break
            case 4: // arrows
            case 5: // bolts
            case 17: // bullets
                weaponLengthCol.visible = true
                missileSpeedCol.visible = true
                maxAmmoCol.visible = true
                abundanceCol.visible = true
                thrustDamageCol.visible = true
                break
            case 6: // shield
                shieldHeightCol.visible = true
                shieldWidthCol.visible = true
                speedRatingCol.visible = true
                hitPointsCol.visible = true
                bodyArmorCol.visible = true
                legArmorCol.visible = true
                headArmorCol.visible = true
                break
            case 7: // bow
            case 8: // crossbow
            case 15: // pistol
            case 16: // musket
                accuracyCol.visible = true
                speedRatingCol.visible = true
                weaponLengthCol.visible = true // ?
                thrustDamageCol.visible = true
                maxAmmoCol.visible = true
                missileSpeedCol.visible = true
                maxAmmoCol.visible = true
                break
            case 9: // thrown
                weaponLengthCol.visible = true
                speedRatingCol.visible = true
                accuracyCol.visible = true
                missileSpeedCol.visible = true
                maxAmmoCol.visible = true
                thrustDamageCol.visible = true
                break
            case 10: // goods
                abundanceCol.visible = true
                maxAmmoCol.visible = true
                foodQualityCol.visible = true
                break
            case 11: // head_armor
                headArmorCol.visible = true
                bodyArmorCol.visible = true
                abundanceCol.visible = true
                break
            case 12: // body_armor
                headArmorCol.visible = true
                bodyArmorCol.visible = true
                legArmorCol.visible = true
                abundanceCol.visible= true
                break
            case 13: // leg_armor
                bodyArmorCol.visible = true
                legArmorCol.visible = true
                abundanceCol.visible= true
                break
            case 14: // hand_armor
                bodyArmorCol.visible = true
                abundanceCol.visible = true
                break
            case 19: // book
                abundanceCol.visible = true
                break
            case 0: // none
            default:
                for (k in stats_and_price_grid.children) {
                    stats_and_price_grid.children[k].visible = true
                }
                break
            }
        }

        GridLayout {
            id: stats_and_price_grid

            columns: 4
            columnSpacing: 4

            ColumnLayout {
                id: priceCol

                Label {
                    text: "Price:"
                }

                SpinBox {
                    id: priceVal
                    Layout.minimumWidth: 48
                    value: 0
                    from: 0
                    to: 999999
                    stepSize: 1
                    editable: true

                    onValueChanged: {
                        curItem.price = priceVal.value
                    }
                }
            }

            ColumnLayout {
                id: weightCol

                Label {
                    text: "Weight:"
                }

                SpinBox {
                    id: weightVal
                    Layout.minimumWidth: 48
                    stepSize: 100
                    editable: true
                    value: 1
                    property int decimals :6;
                    property int min: 0
                    property int max: 99999999
                    from:min*Math.pow(10, decimals)
                    to:max*Math.pow(10, decimals)

                    validator: DoubleValidator {
                        bottom: Math.min(weightVal.from, weightVal.to)
                        top: Math.max(weightVal.from, weightVal.to)
                    }

                    textFromValue: wx

                    valueFromText: wy
                }
            }

            ColumnLayout {
                id: headArmorCol

                Label {
                    text: "Head Armor:"
                }

                SpinBox {
                    id: headArmorVal
                    Layout.minimumWidth: 48
                    value: 0
                    from: 0
                    to: 999999
                    stepSize: 1
                    editable: true

                }
            }

            ColumnLayout {
                id: bodyArmorCol

                Label {
                    text: "Body Armor:"
                }

                SpinBox {
                    id: bodyArmorVal
                    Layout.minimumWidth: 48
                    value: 0
                    from: 0
                    to: 999999
                    stepSize: 1
                    editable: true

                }
            }

            ColumnLayout {
                id: legArmorCol

                Label {
                    text: "Leg Armor:"
                }

                SpinBox {
                    id: legArmorVal
                    Layout.minimumWidth: 48
                    value: 0
                    from: 0
                    to: 999999
                    stepSize: 1
                    editable: true

                }
            }

            ColumnLayout {
                id: difficultyCol

                Label {
                    text: "Difficulty:"
                }

                SpinBox {
                    id: difficultyVal
                    Layout.minimumWidth: 48
                    value: 0
                    from: 0
                    to: 999999
                    stepSize: 1
                    editable: true

                }
            }

            ColumnLayout {
                id: hitPointsCol

                Label {
                    text: "Hit Points:"
                }

                SpinBox {
                    id: hitPointsVal
                    Layout.minimumWidth: 48
                    value: 0
                    from: 0
                    to: 999999
                    stepSize: 1
                    editable: true

                }
            }

            ColumnLayout {
                id : speedRatingCol

                Label {
                    text: "Speed Rating:"
                }

                SpinBox {
                    id: speedRatingVal
                    Layout.minimumWidth: 48
                    value: 0
                    from: 0
                    to: 999999
                    stepSize: 1
                    editable: true

                }
            }

            ColumnLayout {
                id: missileSpeedCol

                Label {
                    text: "Missile Speed:"
                }

                SpinBox {
                    id: missileSpeedVal
                    Layout.minimumWidth: 48
                    value: 0
                    from: 0
                    to: 999999
                    stepSize: 1
                    editable: true

                }
            }

            ColumnLayout {
                id: weaponLengthCol

                Label {
                    text: "Weapon Length:"
                }

                SpinBox {
                    id: weaponLengthVal
                    Layout.minimumWidth: 48
                    value: 0
                    from: 0
                    to: 999999
                    stepSize: 1
                    editable: true

                }
            }

            ColumnLayout {
                id: shieldWidthCol

                Label {
                    text: "Shield Width:"
                }

                SpinBox {
                    id: shieldWidthVal
                    Layout.minimumWidth: 48
                    value: 0
                    from: 0
                    to: 999999
                    stepSize: 1
                    editable: true

                }
            }

            ColumnLayout {
                id: shieldHeightCol

                Label {
                    text: "Shield Height:"
                }

                SpinBox {
                    id: shieldHeightVal
                    Layout.minimumWidth: 48
                    value: 0
                    from: 0
                    to: 999999
                    stepSize: 1
                    editable: true

                }
            }

            ColumnLayout {
                id: maxAmmoCol

                Label {
                    text: "Max Ammo:"
                }

                SpinBox {
                    id: maxAmmoVal
                    Layout.minimumWidth: 48
                    value: 0
                    from: 0
                    to: 999999
                    stepSize: 1
                    editable: true

                }
            }

            ColumnLayout {
                id: horseScaleCol

                Label {
                    text: "Horse Scale:"
                }

                SpinBox {
                    id: horseScaleVal
                    Layout.minimumWidth: 48
                    value: 0
                    from: 0
                    to: 999999
                    stepSize: 1
                    editable: true

                }
            }

            ColumnLayout {
                id: horseSpeedCol

                Label {
                    text: "Horse Speed:"
                }

                SpinBox {
                    id: horseSpeedVal
                    Layout.minimumWidth: 48
                    value: 0
                    from: 0
                    to: 999999
                    stepSize: 1
                    editable: true

                }
            }

            ColumnLayout {
                id: horseManeuverCol

                Label {
                    text: "Horse Maneuver:"
                }

                SpinBox {
                    id: horseManeuverVal
                    Layout.minimumWidth: 48
                    value: 0
                    from: 0
                    to: 999999
                    stepSize: 1
                    editable: true

                }
            }

            ColumnLayout {
                id: horseChargeCol

                Label {
                    text: "Horse Charge:"
                }

                SpinBox {
                    id: horseChargeVal
                    Layout.minimumWidth: 48
                    value: 0
                    from: 0
                    to: 999999
                    stepSize: 1
                    editable: true

                }
            }

            ColumnLayout {
                id: foodQualityCol

                Label {
                    text: "Food Quality:"
                }

                SpinBox {
                    id: foodQualityVal
                    Layout.minimumWidth: 48
                    value: 0
                    from: 0
                    to: 999999
                    stepSize: 1
                    editable: true

                }
            }

            ColumnLayout {
                id: abundanceCol

                Label {
                    text: "Abundance:"
                }

                SpinBox {
                    id: abundanceVal
                    Layout.minimumWidth: 48
                    value: 0
                    from: 0
                    to: 999999
                    stepSize: 1
                    editable: true

                }
            }

            ColumnLayout {
                id: accuracyCol

                Label {
                    text: "Accuracy:"
                }

                SpinBox {
                    id: accuracyVal
                    Layout.minimumWidth: 48
                    value: 0
                    from: 0
                    to: 999999
                    stepSize: 1
                    editable: true

                }
            }

            ColumnLayout {
                id: swingDamageCol

                Label {
                    text: "Swing Damage:"
                }

                SpinBox {
                    id: swingDamageVal
                    Layout.minimumWidth: 48
                    value: 0
                    from: 0
                    to: 999999
                    stepSize: 1
                    editable: true

                }

                ComboBox {
                    id: swingDamageType

                    model: [
                        "CUT",
                        "PIERCE",
                        "BLUNT"
                    ]
                }
            }

            ColumnLayout {
                id: thrustDamageCol

                Label {
                    text: "Thrust Damage:"
                }

                SpinBox {
                    id: thrustDamageVal
                    Layout.minimumWidth: 48
                    value: 0
                    from: 0
                    to: 999999
                    stepSize: 1
                    editable: true

                }

                ComboBox {
                    id: thrustDamageType

                    model: [
                        "CUT",
                        "PIERCE",
                        "BLUNT"
                    ]
                }
            }

        }
    }

}
