from os import truncate
import PySimpleGUI as sig
import scrap3
import re
import logging as log
import threading as th

class Windows:

    def __init__(self):
        # window tema
        sig.theme('BluePurple')
        self.width = 700
        self.height = 300
        self.w_pad = (self.width / 7, 0)
        self.done = False

    def layout(self):
        L1 = [
            [sig.Text("都道府県　※「都道府県ごと」か「全国」の選択可",
                      key='pref_title', size=(60, None))],
            [sig.InputText(key=('pref_name'))],
            [sig.Text("ジャンル選択", key="class_title", size=(60, None)), ],
            [sig.InputOptionMenu(self.menu_list(), key=(
                "store_class"), size=(40, None))]
        ]

        L2 = [
            [sig.Text("フォルダ選択", key='path_title', size=(60, None))],
            [sig.InputText(key='path'), sig.FolderBrowse("選択")]
        ]
        L = [
            [sig.Frame("抽出条件", L1)],
            [sig.Frame("保存先", L2)],
            [sig.Button("抽出実行")]
        ]
        return L
    def pop_layout(self):
        L = [
            [sig.Text("抽出実行中…")],
            [sig.ProgressBar(1000, orientation="h", size=(20, 20), key="progbar")],
            [sig.Cancel('中止')],
        ]
        return L

    def menu_list(self):
        class_menu = [
            "ヘアサロン",
            "ネイル・まつげサロン",
            "リラクサロン",
            "エステサロン",
            "美容クリニック",
            "すべてのジャンル"
            ]
        return class_menu

    def display(self):
        self.win = sig.Window("HotPepperBeautyスクレイピングツール", self.layout(), icon="icon2.ico")
        while True:
            self.event, self.value = self.win.read()
            print(self.event, self.value)
            if self.event == '抽出実行':
                check = self.input_checker()
                if check:
                    th1 = th.Thread(target=scrap3.main, args=(self.value['path'], self.value['pref_name'], self.value['store_class']))
                    th1.start()
                    #self.pop_display()
            #when window close
            if self.event in ("Quit", None):
                break
        self.win.close()
    
    def pop_display(self):
        self.sub_win = sig.Window("スクレイピング進行状況", self.pop_layout(), icon="icon2.ico")
        while True:
            sub_event = self.sub_win.read(timeout=10)
            if sub_event in (None, '中止'):
                break
            self.progress_bar(scrap3.Job.scrap_counter)
        self.sub_win.close()

    def progress_bar(self, percent):
        self.sub_win['progbar'].update_bar(percent)

    def input_checker(self):
        checker = [False, False, False]
        if self.value['pref_name'] == "" or re.fullmatch('東京都|北海道|(?:京都|大阪)府|.{2,3}県', self.value['pref_name']) == None:
            text2 = "都道府県　※入力値が不正です。例）東京都, 北海道, 大阪府"
            self.win['pref_title'].update(text2, text_color='red')
            self.win['pref_name'].update(background_color='red')
        else:
            text2 = "都道府県"
            self.win['pref_title'].update(text2, text_color='purple')
            self.win['pref_name'].update(background_color = 'white')
            checker[0] = True
        if self.value['store_class'] == "":
            self.win['class_title'].update("ジャンル選択　※選択必須です。", text_color='red')
            # win['store_class'].update(background_color = 'red')
        else:
            self.win['class_title'].update("ジャンル選択", text_color='purple')
            checker[1] = True
        if self.value['path'] == "":
            self.win['path_title'].update('フォルダ選択 ※保存先が選択されていません。',text_color='red')
            self.win['path'].update(background_color="red")
        else:
            self.win['path_title'].update(text_color='purple')
            self.win['path'].update(background_color="white")
            checker[2] = True
        
        if False in checker:
            return False
        else:
            return True
"""
class PopupWindow(MainWindow):

    def __init__(self):
        self.width = 600
        self.height = 400
        self.prg_per = 0
    
    def layout(self):
        L = [
            [sig.Text("抽出実行中…")],
            [sig.ProgressBar(1000, orientation="h", size=(20, 20), key="progbar")],
            [sig.Cancel('中止')],
        ]
        return L 
    
    def display(self):
        self.win = sig.Window("スクレイピング進行状況", self.layout(), icon="icon2.ico")
        done = False
        while self.prg_per <= 100:
            sub_event = self.win.read(timeout=10)    
            print(sub_event)
            if sub_event in (None, '中止'):
                break
            self.progress_bar(scrap3.Job.scrap_counter)
        self.win.close()

    def progress_bar(self, percent):
        self.win['progbar'].update_bar(percent)
"""    
main_win = Windows()
main_win.display()



