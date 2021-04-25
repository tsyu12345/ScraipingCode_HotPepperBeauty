import PySimpleGUI as sig
from PySimpleGUI.PySimpleGUI import theme_background_color, theme_input_background_color
# from scrap import Job

# window tema
sig.theme('BluePurple')
# setting window option
width = 700
height = 300
w_pad = (width / 7, 0)

menu = ["ヘアサロン", "ネイル・まつげサロン", "リラクサロン", "エステサロン", "美容クリニック", "すべてのジャンル"]

L1 = [
    [sig.Text("都道府県　※「都道府県ごと」か「全国」の選択可　　　　　　", key='pref_title')],
    [sig.InputText(key=('pref_name'))],
    [sig.Text("ジャンル選択　　　　　　　　　　　　　　　　　　　　", key="class_title"),],
    [sig.OptionMenu(menu, key=("store_class"), size=(40, ))]
]

L2 = [
    [sig.Text("フォルダ選択")],
    [sig.InputText(key='path'), sig.FolderBrowse("選択")]
]

L = [
    [sig.Frame("抽出条件", L1)],
    [sig.Frame("保存先", L2)],
    [sig.Button("抽出実行")]
]

win = sig.Window("HotPepperBeautyスクレイピングツール", L, icon="icon2.ico")
print(win)
while True:
    event, value = win.read()
    print(event)
    print(value)
    #check
    if event == '抽出実行':
        if value['pref_name'] == "":
            text2 = "都道府県　※入力値が不正です。例）東京都, 北海道, 全国"
            win['pref_title'].update(text2, text_color='red')
            win['pref_name'].update(background_color = 'red')
        else:
            text2 = "都道府県"
            win['pref_title'].update(text2, text_color='purple')
            win['pref_name'].update(background_color = 'white')
        if value['store_class'] == "":
            win['class_title'].update("ジャンル選択　※選択必須です。", text_color='red')
        else:
            win['class_title'].update("ジャンル選択", text_color='purple')
        if value['path'] == "":
            win['path'].update(background_color="red")
        else:
            win['path'].update(background_color="purple")
    
    #when window close
    if event in ("Quit", None):
        break

win.close()
