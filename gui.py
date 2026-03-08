import FreeSimpleGUI as sg

label1 = sg.Text("Enter feet")
box1 = sg.InputText(tooltip="Enter feet", key="feet")

label2 = sg.Text("Enter Inches")
box2 = sg.InputText(tooltip="Inches", key="inches")
button = sg.Button("Convert")
clearButton = sg.Button("Clear")
label3 = sg.Text("", key="output")

window = sg.Window("Converter",
                   layout=[[label1, box1], [label2, box2], [button, clearButton, label3]],
                   font=('Helvetica', 20))
while True:
    event, value = window.read()
    print(f"event: {event}")
    print(f"value: {value}")
    match event:
        case "Convert":
            feet = 0 if value.get("feet",'0') == '' else value.get("feet",'0')
            inch = 0 if value.get("inches",'0') == '' else value.get("inches",'0')

            print(inch, feet)
            meters = float(feet)*0.3048 + float(inch)*0.0254
            window["output"].update(value=meters)
            # if value["feet"] != '':
            #     feet = float(value["feet"])
            #     inch = 12 * feet
            #     print(inch)
            #     window["inches"].update(value=inch)
            #     window["output"].update(value=inch)
            # else:
            #     inch = float(value["inches"])
            #     feet = inch / 12
            #     print(feet)
            #     window["feet"].update(value=feet)
        case sg.WIN_CLOSED:
            break
        case "Clear":
            window["inches"].update(value='')
            window["feet"].update(value='')
            window["output"].update(value='')

window.close()