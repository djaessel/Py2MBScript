import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts

Rectangle {
  //anchors.fill: parent
  color: "#223344"

TabBar {
  id: bar
  width: parent.width
  
  TabButton {
    text: "Source Code"
  }
  TabButton {
    text: "Module Items"
  }
}

StackLayout {
  id: root
  width: parent.width
  anchors.top: parent.top
  anchors.topMargin: 28
  currentIndex: bar.currentIndex


  Flickable {
     id: flickable
     flickableDirection: Flickable.VerticalFlick
     height: 800
     width: 400
     //contentHeight: textArea.height + 20
     //contentWidth: 400

     TextArea.flickable: TextArea {
            id: textArea
            textFormat: Qt.RichText
            wrapMode: TextArea.Wrap
            focus: true
            selectByMouse: true
            persistentSelection: true
            // Different styles have different padding and background
            // decorations, but since this editor is almost taking up the
            // entire window, we don't need them.
            leftPadding: 6
            rightPadding: 6
            topPadding: 6
            bottomPadding: 0
            background: null
            anchors.fill: parent
            

	    text: "TEST 123.\nTEST 123?\nTEST 123!\n"

	    property bool processing: true

            onTextChanged: {
                if (!processing) {
                    processing = true;
                    let p = cursorPosition;
                    let markUp = getText(0, length).replace(
                      /([A-Z][A-Za-z]*|[a-z][A-Za-z]*|[0-9]+|[ \t\n]|['][^']*[']|[^A-Za-z0-9\t\n ])/g,
                        function (f) {
                            //console.log("f: ", JSON.stringify(f));

                            //if (commnds.includes(f)){
                            //    popper.x = textArea.cursorRectangle.x;
                            //    popper.y = textArea.cursorRectangle.y;
                            //    popper.visible = true;
                            //    return "<span style='color:#2288dd'>" + f + "</span>";
                            //}
                            /*else */if (f.match(/^[A-Z][A-Za-z]*$/))
                                return "<span style='color:#dd00aa'>" + f + "</span>";
                            else if (f.match(/^[a-z][A-Za-z]*$/))
                                return "<span style='color:#dd0000'>" + f + "</span>";
                            else if (f.match(/^[0-9]+$/))
                                return "<span style='color:#00bbff'>" + f + "</span>";
                            else if (f.match(/^[ ]/))
                                return "&nbsp;"
                            //else if (f.match(/^[\t\n]/))
                            //    return f;
                            else if (f.match(/^[']/))
                                return "<span style='color:#008000'>" + f + "</span>";
                            else
                                return f;
                        }
                    );
                    text = markUp;
                    cursorPosition = p;
                    processing = false;
                }
            }

            Text {
                id: popper
                text: "Hello!"
                visible: false
            }
     }

     ScrollBar.vertical: ScrollBar { }
  }

  Item {
    id: currentModuleName

    Rectangle {
        id: controlRoot

        property int count: 0

        Component.onCompleted: {
		createButton(0)
		createButton(1)
        }

	function createButton(xEx) {
            wonderButton.createObject(controlRoot, { width: 200, x: xEx * 208 + 16, text: "Count" + (xEx+1) })
            count += 1
        }

    }

    Component {
        id: wonderButton
        Button {
            text: "TEST"
        }
    }
  }
}
}
