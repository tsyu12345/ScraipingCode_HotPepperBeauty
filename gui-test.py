import PySimpleGUI as gui
from PySimpleGUI.PySimpleGUI import Window 

layout = [
    [gui.Text("BIG UNNKO")],
    [gui.Text("World")],
    [gui.InputText(key="-IN-")],
    [gui.Submit(), gui.Cancel()]
]

window = gui.Window-("test-gui", layout=layout, size=(400, 400))

event, val = window.read()
window.close()

text_in = val["-IN-"]
gui.popup("OKi", text_in)