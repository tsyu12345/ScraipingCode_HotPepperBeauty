import PySimpleGUI as sg

L1 = [
    [sg.Button('A', size=(5, 1)), sg.Button('B', size=(5, 1))]
    ]

L=[[sg.Frame('Group 1',L1)]]

window = sg.Window('psguiFrame02.py ', L)

while True:
    event, value = window.read()
    print(value)
    if event in ("Quit", None):
        break
window.close()