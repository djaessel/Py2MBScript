import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

RowLayout {
    id: meshRoot
    spacing: 0

    property string idText: ""
    property string resourceName: ""
    property int meshKind: 0
    property string modifiers: "0"
    property bool show: true

    Label {
        Layout.minimumWidth: 64
        text: meshRoot.idText
        horizontalAlignment: Text.AlignHCenter
    }

    TextEdit {
        Layout.minimumWidth: 300
        text: meshRoot.resourceName
        horizontalAlignment: Text.AlignHCenter
    }

    ComboBox {
        Layout.minimumWidth: 200
        model: [
            "Default",
            "Inventory",
            "Flying Ammo",
            "Carry",
        ]
        currentIndex: meshRoot.meshKind
    }

    TextEdit {
        Layout.minimumWidth: 200
        text: meshRoot.modifiers
        horizontalAlignment: Text.AlignHCenter
    }

    CheckBox {
        Layout.minimumWidth: 64
        checked: meshRoot.show
    }

    Button {
        Layout.minimumWidth: 32
        flat: true
        text: "X"
        onClicked: {
            let idx = 0
            for (var k in curItem.meshes) {
                if (curItem.meshes[k].id == meshRoot.resourceName) {
                    curItem.meshes.splice(idx, 1)
                    break
                }
                idx += 1
            }
            meshRoot.destroy()
        }
    }
}
