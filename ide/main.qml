import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts

import "."


Rectangle {
  id: root
  color: "#223344"

 TabBar {
  id: bar
  width: parent.width
  
  TabButton {
    text: "Source Code"

    onClicked: {
       root.color = "#223344"
    }
  }
  TabButton {
    text: "Module Items"

    onClicked: {
       root.color = "grey"
    }
  }
 }

 StackLayout {
  id: stackRoot
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
            
	    text: itemsCode

	    property bool processing: false

	    property var keywordsx: ["from", "import"]

            onTextChanged: {
                if (!processing) {
                    processing = true;
                    let p = cursorPosition;
		    let markUp = getText(0, length)
                    markUp = markUp.replace(
                      /(#.*|[.][a-zA-Z_]+[(]|[A-Z][A-Za-z_\-]*|[a-z][A-Za-z_\-]*|[0-9.]+|["'][A-Za-z ./_\-]*["']|[^A-Za-z0-9\t\n ])/g,
                        function (f) {
                            //console.log("f: ", JSON.stringify(f));
                            //if (commnds.includes(f)){
                            //    popper.x = textArea.cursorRectangle.x;
                            //    popper.y = textArea.cursorRectangle.y;
                            //    popper.visible = true;
                            //    return "<span style='color:#2288dd'>" + f + "</span>";
                            //}
			    if (keywordsx.includes(f)){
				return "<span style='color:#2288dd'>" + f + "</span>";
			    }
			    else if (f.match(/^#.*/))
                                return "<span style='color:#008000'>" + f + "</span>";
                            else if (f.match(/^['"][A-Za-z ./_\-]+['"]$/))
                                return "<span style='color:#00a000'>" + f + "</span>";
                            else if (f.match(/^[A-Z][A-Za-z _\-]*$/))
                                return "<span style='color:#ddaabb'>" + f + "</span>";
                            else if (f.match(/^[a-z][A-Za-z _\-]*$/))
                                return "<span style='color:#ddeedd'>" + f + "</span>";
			    else if (f.match(/^[.][a-zA-Z_]+[(]/))
				return "<span style='color:#ddaa44'>" + f.replace("(","") + "</span>(";
                            else if (f.match(/^[0-9.]+$/))
                                return "<span style='color:#00bbff'>" + f + "</span>";
                            else if (f.match(/^[ ]/))
                                return "&nbsp;"
                            //else if (f.match(/^[\t\n]/))
                            //    return f;
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

        Component.onCompleted: {
		var newModel = []
                for (var itm in xitems) {
		    newModel.push({value: xitems[itm].meshes[0].id, text: xitems[itm].id})
                }
		coolcombo.model = newModel
        }

	ComboBox {
	    id: coolcombo
	    x: 8
	    y: 8
            width: 200
            textRole: "text"
            valueRole: "value"
	    //editable: true
	    onActivated: {
                var x = "select:mesh:" + currentValue
		tcpSender.send(x)
	    }
	    model: []
	    onCurrentIndexChanged: {
                        var curIdx = 0
                        for (var x in xitems) {
                                if (curIdx == coolcombo.currentIndex) {
                                        itemManager.curItem = xitems[x]
                                        break
                                }
                                curIdx += 1
                        }
	    }
	}

	ItemManager {
		id: itemManager
		y: coolcombo.height + coolcombo.y + 16
		x: 8
	}

    }
  }
 }
}
