import PySimpleGUI as sig 
#from scrap import Job

layout = [
    [sig.Text("エリア入力"),],
    [sig.Input(key='-IN1-')],
    [sig.Text("抽出ジャンル選択")],
    [sig.OptionMenu(["ヘアサロン", "ネイル・まつげサロン", "リラクサロン", "エステサロン", "美容クリニック","すべてのジャンル"])],
    [sig.Text("保存先を選択"), sig.InputText(), sig.FolderBrowse(key="save_folder")],
    [sig.Button("抽出実行")]

]

sig.theme('SystemDefault')
width = 700
height = 300
win = sig.Window(title="HotPepperBeautyスクレイピングツール", layout=layout, size=(width, height))
while True:
    event, value = win.read()
    if event in ("Quit", None):
       break
win.close()