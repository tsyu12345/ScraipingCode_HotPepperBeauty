from calendar import THURSDAY
import PySimpleGUI as sig
import scrap3
import re
import logging as log
import threading as th
import sys

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
            [sig.ProgressBar(100, orientation="h", size=(20, 20), key="progbar")],
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
        self.sub_win = sig.Window("抽出実行", self.pop_layout(), icon="icon2.ico")
        count = 0
        i = 0
        while True:
            self.event, self.value = self.win.read()
            th1 = th.Thread(target=scrap3.main, args=(self.value['path'], self.value['pref_name'], self.value['store_class']))
            print(self.event, self.value)
            if self.event == '抽出実行':
                check = self.input_checker()
                if check:
                    i += 1
                    th1.setDaemon(True)
                    th1.start()
                    count = 1
                    #sub_event, sub_value = self.sub_win.read()
                    #self.sub_win['progbar'].update_bar(50)
                    cancel = sig.popup_cancel('抽出処理中です。これには数時間かかることがあります。\n中断するには’Cancelled’ボタンを押してください。')
                    print(cancel)
                    if cancel in ('Cancelled', None):
                        sys.exit()
            #th1.join()
                    self.done = True
                    #sig.popup('お疲れ様でした。抽出終了です。ファイルを確認してください。\n保存先：'+self.value['path'], keep_on_top=True)
            #when window close
            if self.event in ("Quit", None) or self.done:
                break
        self.win.close()

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



