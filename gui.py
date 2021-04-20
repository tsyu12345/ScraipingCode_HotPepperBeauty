import PySimpleGUI as sig 
#from main import Job

layout = [
    [sig.Text("エリア入力"),],
    [sig.Input(key='-IN1-')],
    [sig.Text("抽出ジャンル選択")],
    [sig.Text("準備中")],
    [sig.Text("保存先を選択"), sig.InputText(), sig.FolderBrowse(key="save_folder")],
    [sig.Button("抽出開始")]

]

width = 700
height = 300
win = sig.Window(title="HotPepperBeautyスクレイピングツール", layout=layout, size=(width, height))
while True:
    event, value = win.read()
    if event in ("Quit", None):
       break
win.close()