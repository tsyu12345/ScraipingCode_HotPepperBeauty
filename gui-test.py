import PySimpleGUI as sg

layout = [
    [sg.Text("A custom progress meter")],
    [sg.ProgressBar(100, orientation="h", size=(20, 20), key="progbar")],
    [sg.Cancel('中止')],
]

window = sg.Window("Custom Progress Meter", layout)
prg = 0
while prg <= 100:
    event, values = window.read(timeout=2)
    if event == "中止" or event is None:
        break
    prg += 1
    print(values)
    window["progbar"].update_bar(prg)
