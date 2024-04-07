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
            "TEST123",
            "TEST456",
            "TEST789",
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
            console.log(JSON.stringify(curItem.meshes))
            curItem.meshes.splice(parseInt(idText)-1, 1)
            console.log(JSON.stringify(curItem.meshes))
            meshRoot.destroy()
        }
    }
}
