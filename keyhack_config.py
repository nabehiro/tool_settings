# -*- mode: python; coding: utf-8-dos -*-

##
## Windows の操作を emacs のキーバインドで行うための設定（keyhac版）
##

#
# emacs の挙動と明らかに違う動きの部分は以下のとおりです。
# ・左の Ctrlキー と Altキー のみが、emacs用のキーとして認識される。
# ・ESC の二回押下で、ESC を入力できる。
# ・C-c、C-z は、Windows の「コピー」、「取り消し」が機能するようにしている。
# ・C-x C-y で、クリップボード履歴を表示する。（C-n で選択を移動し、Enter で確定する）
# ・C-x o は、一つ前にフォーカスがあったウインドウに移動する。
#   NTEmacs から Windowsアプリケーションソフトを起動した際に戻るのに便利。
# ・C-k を連続して実行しても、クリップボードへの削除文字列の蓄積は行われない。
#   C-u による行数指定をすると、削除行を一括してクリップボードに入れることができる。
#   この設定では、Sakura Editor のみ対応している。
# ・キーボードマクロは emacs の挙動と異なり、IME の変換キーも含めた入力したキー
#   そのものを記録する。このため、キーボードマクロ記録時や再生時、IMEの状態に留意した
#   利用が必要。
# ・Excel の場合、^Enter に F2（セル編集モード移行）を割り当てている。（オプション）
# ・Emacs の場合、IME 切り替え用のキーを C-\ に置き換える方法を提供している。（オプション）

from time   import sleep
from keyhac import *

def configure(keymap):

    # すべてのアプリケーションが対象
    keymap_emacs = keymap.defineWindowKeymap()

    # mark がセットされると True になる
    keymap_emacs.is_marked = False

    # 検索が開始されると True になる
    keymap_emacs.is_searching = False

    # universal-argument コマンドが実行されると True になる
    keymap_emacs.is_universal_argument = False

    # digit-argument コマンドが実行されると True になる
    keymap_emacs.is_digit_argument = False

    # コマンドのリピート回数を設定する
    keymap_emacs.repeat_counter = 1

    ########################################################################
    ## IMEの切替え
    ########################################################################

    def toggle_input_method():
        keymap.InputKeyCommand("A-(25)")()

    ########################################################################
    ## ファイル操作
    ########################################################################

    def find_file():
        keymap.InputKeyCommand("C-o")()

    def save_buffer():
        keymap.InputKeyCommand("C-s")()

    def write_file():
        keymap.InputKeyCommand("A-f", "A-a")()

    def new_buffer():
        keymap.InputKeyCommand("C-n")()

    ########################################################################
    ## カーソル移動
    ########################################################################

    def backward_char():
        keymap.InputKeyCommand("Left")()

    def forward_char():
        keymap.InputKeyCommand("Right")()

    def backward_word():
        keymap.InputKeyCommand("C-Left")()

    def forward_word():
        keymap.InputKeyCommand("C-Right")()

    def previous_line():
        keymap.InputKeyCommand("Up")()

    def next_line():
        keymap.InputKeyCommand("Down")()

    def move_beginning_of_line():
        keymap.InputKeyCommand("Home")()

    def move_end_of_line():
        keymap.InputKeyCommand("End")()

    def beginning_of_buffer():
        keymap.InputKeyCommand("C-Home")()

    def end_of_buffer():
        keymap.InputKeyCommand("C-End")()

    def scroll_up():
        keymap.InputKeyCommand("PageUp")()

    def scroll_down():
        keymap.InputKeyCommand("PageDown")()

    ########################################################################
    ## カット / コピー / 削除 / アンドゥ
    ########################################################################

    def delete_backward_char():
        keymap.InputKeyCommand("Back")()

    def delete_char():
        keymap.InputKeyCommand("Delete")()

    def backward_kill_word():
        keymap.InputKeyCommand("C-S-Left", "C-x")()

    def kill_word():
        keymap.InputKeyCommand("C-S-Right", "C-x")()

    def kill_line():
        keymap_emacs.is_marked = True
        mark(move_end_of_line)()
        keymap.InputKeyCommand("C-c", "Delete")()

    def kill_line2():
        if keymap_emacs.repeat_counter == 1:
            kill_line()
        else:
            keymap_emacs.is_marked = True
            for i in range(keymap_emacs.repeat_counter - 1):
                mark(next_line)()
            mark(move_end_of_line)()
            mark(forward_char)()
            kill_region()

    def kill_region():
        keymap.InputKeyCommand("C-x")()

    def kill_ring_save():
        keymap.InputKeyCommand("C-c")()
        keymap.InputKeyCommand("Esc")()

    def windows_copy():
        keymap.InputKeyCommand("C-c")()

    def yank():
        keymap.InputKeyCommand("C-v")()

    def undo():
        keymap.InputKeyCommand("C-z")()

    def set_mark_command():
        if keymap_emacs.is_marked:
            keymap_emacs.is_marked = False
        else:
            keymap_emacs.is_marked = True

    def mark_whole_buffer():
        if keymap.getWindow().getClassName().startswith("EXCEL"): # Microsoft Excel
            # Excel のセルの中でも機能するようにする対策
            keymap.InputKeyCommand("C-End", "C-S-Home")()
        else:
            keymap.InputKeyCommand("C-Home", "C-a")()

    def mark_page():
        mark_whole_buffer()

    def open_line():
        keymap.InputKeyCommand("Enter", "Up", "End")()

    ########################################################################
    ## バッファ / ウインドウ操作
    ########################################################################

    def kill_buffer():
        keymap.InputKeyCommand("C-F4")()

    def other_window():
        keymap.InputKeyCommand("D-Alt")()
        keymap.InputKeyCommand("Tab")()
        sleep(0.01) # delay
        keymap.InputKeyCommand("U-Alt")()

    ########################################################################
    ## 文字列検索 / 置換
    ########################################################################

    def replace():
        keymap.InputKeyCommand("C-h")()

    def isearch_backward():
        if keymap_emacs.is_searching:
            if keymap.getWindow().getProcessName() == "EXCEL.EXE":  # Microsoft Excel
                if keymap.getWindow().getClassName() == "EDTBX": # 検索ウィンドウ
                    keymap.InputKeyCommand("A-S-f")()
                else:
                    keymap.InputKeyCommand("C-f")()
            else:
                keymap.InputKeyCommand("S-F3")()
        else:
            keymap.InputKeyCommand("C-f")()
            keymap_emacs.is_searching = True

    def isearch_forward():
        if keymap_emacs.is_searching:
            if keymap.getWindow().getProcessName() == "EXCEL.EXE":  # Microsoft Excel
                if keymap.getWindow().getClassName() == "EDTBX": # 検索ウィンドウ
                    keymap.InputKeyCommand("A-f")()
                else:
                    keymap.InputKeyCommand("C-f")()
            else:
                keymap.InputKeyCommand("F3")()
        else:
            keymap.InputKeyCommand("C-f")()
            keymap_emacs.is_searching = True

    ########################################################################
    ## その他
    ########################################################################

    def newline():
        keymap.InputKeyCommand("Enter")()

    def newline_and_indent():
        keymap.InputKeyCommand("Enter", "Tab")()

    def indent_for_tab_command():
        keymap.InputKeyCommand("Tab")()

    def keybord_quit():
        if not keymap.getWindow().getClassName().startswith("EXCEL"): # Microsoft Excel 以外
            # 選択されているリージョンのハイライトを解除するために Esc を発行しているが、
            # アプリケーションソフトによっては効果なし
            keymap.InputKeyCommand("Esc")()
        keymap.command_RecordStop()

    def kill_emacs():
        keymap.InputKeyCommand("A-F4")()

    def universal_argument():
        if keymap_emacs.is_universal_argument == True:
            if keymap_emacs.is_digit_argument == True:
                keymap_emacs.is_universal_argument = False
            else:
                keymap_emacs.repeat_counter = keymap_emacs.repeat_counter * 4
        else:
            keymap_emacs.is_universal_argument = True
            keymap_emacs.repeat_counter = keymap_emacs.repeat_counter * 4

    def digit_argument(number):
        if keymap_emacs.is_digit_argument == True:
            keymap_emacs.repeat_counter = keymap_emacs.repeat_counter * 10 + number
        else:
            keymap_emacs.repeat_counter = number
            keymap_emacs.is_digit_argument = True

    def clipboard_list():
        keymap_emacs.is_marked = False
        keymap.command_ClipboardList()

    ########################################################################
    ## 共通関数
    ########################################################################

    def self_insert_command(key):
        return keymap.InputKeyCommand(key)

    def digit(number):
        def _digit():
            if keymap_emacs.is_universal_argument == True:
                digit_argument(number)
            else:
                reset_counter(reset_mark(repeat(keymap.InputKeyCommand(str(number)))))()
        return _digit

    def digit2(number):
        def _digit2():
            keymap_emacs.is_universal_argument = True
            digit_argument(number)
        return _digit2

    def mark(func):
        def _mark():
            if keymap_emacs.is_marked:
                # D-Shift だと、M-< や M-> 押下時に、D-Shift が解除されてしまう。その対策。
                keymap.InputKeyCommand("D-LShift")()
                keymap.InputKeyCommand("D-RShift")()
            func()
            if keymap_emacs.is_marked:
                keymap.InputKeyCommand("U-LShift")()
                keymap.InputKeyCommand("U-RShift")()
        return _mark

    def reset_mark(func):
        def _reset_mark():
            func()
            keymap_emacs.is_marked = False
        return _reset_mark

    def reset_counter(func):
        def _reset_counter():
            func()
            keymap_emacs.is_universal_argument = False
            keymap_emacs.is_digit_argument = False
            keymap_emacs.repeat_counter = 1
        return _reset_counter

    def reset_search(func):
        def _reset_search():
            func()
            keymap_emacs.is_searching = False
        return _reset_search

    def repeat(func):
        def _repeat():
            repeat_counter = keymap_emacs.repeat_counter
            keymap_emacs.repeat_counter = 1
            for i in range(repeat_counter):
                func()
        return _repeat

    def repeat2(func):
        def _repeat2():
            if keymap_emacs.is_marked == True:
                keymap_emacs.repeat_counter = 1
            repeat(func)()
        return _repeat2

    ########################################################################
    ## キーバインド
    ########################################################################

    # http://homepage3.nifty.com/ic/help/rmfunc/vkey.htm
    # http://www.azaelia.net/factory/vk.html

    ## マルチストロークキーの設定
    keymap_emacs["Esc"]            = keymap.defineMultiStrokeKeymap("Esc")
    keymap_emacs["LC-OpenBracket"] = keymap.defineMultiStrokeKeymap("C-OpenBracket")
    keymap_emacs["LC-x"]           = keymap.defineMultiStrokeKeymap("C-x")
    keymap_emacs["LC-q"]           = keymap.defineMultiStrokeKeymap("C-q")

    ## SPACE, A-Zキーの設定
    for vkey in [32] + list(range(65, 90 + 1)):
        keymap_emacs[  "(" + str(vkey) + ")"] = reset_counter(reset_mark(repeat(self_insert_command(  "(" + str(vkey) + ")"))))
        keymap_emacs["S-(" + str(vkey) + ")"] = reset_counter(reset_mark(repeat(self_insert_command("S-(" + str(vkey) + ")"))))

    ## 10key の特殊文字キーの設定
    for vkey in [106, 107, 109, 110, 111]:
        keymap_emacs[  "(" + str(vkey) + ")"] = reset_counter(reset_mark(repeat(self_insert_command(  "(" + str(vkey) + ")"))))

    ## 特殊文字キーの設定
    for vkey in list(range(186, 192 + 1)) + list(range(219, 222 + 1)) + [226]:
        keymap_emacs[  "(" + str(vkey) + ")"] = reset_counter(reset_mark(repeat(self_insert_command(  "(" + str(vkey) + ")"))))
        keymap_emacs["S-(" + str(vkey) + ")"] = reset_counter(reset_mark(repeat(self_insert_command("S-(" + str(vkey) + ")"))))

    ## quoted-insertキーの設定
    for vkey in range(1, 255):
        keymap_emacs["LC-q"][  "("   + str(vkey) + ")"] = reset_search(reset_counter(reset_mark(repeat(self_insert_command(  "("   + str(vkey) + ")")))))
        keymap_emacs["LC-q"]["S-("   + str(vkey) + ")"] = reset_search(reset_counter(reset_mark(repeat(self_insert_command("S-("   + str(vkey) + ")")))))
        keymap_emacs["LC-q"]["C-("   + str(vkey) + ")"] = reset_search(reset_counter(reset_mark(repeat(self_insert_command("C-("   + str(vkey) + ")")))))
        keymap_emacs["LC-q"]["C-S-(" + str(vkey) + ")"] = reset_search(reset_counter(reset_mark(repeat(self_insert_command("C-S-(" + str(vkey) + ")")))))
        keymap_emacs["LC-q"]["A-("   + str(vkey) + ")"] = reset_search(reset_counter(reset_mark(repeat(self_insert_command("A-("   + str(vkey) + ")")))))
        keymap_emacs["LC-q"]["A-S-(" + str(vkey) + ")"] = reset_search(reset_counter(reset_mark(repeat(self_insert_command("A-S-(" + str(vkey) + ")")))))

    ## Esc の二回押しを Esc とする設定
    keymap_emacs["Esc"]["Esc"]                      = reset_counter(self_insert_command("Esc"))
    keymap_emacs["LC-OpenBracket"]["C-OpenBracket"] = reset_counter(self_insert_command("Esc"))

    ## universal-argumentキーの設定
    keymap_emacs["LC-u"] = universal_argument

    ## 「IMEの切替え」のキー設定
    keymap_emacs["(243)"]   = toggle_input_method
    keymap_emacs["(244)"]   = toggle_input_method
    keymap_emacs["LA-(25)"] = toggle_input_method
    keymap_emacs["LC-o"]    = open_line

    ## 「ファイル操作」のキー設定
    keymap_emacs["LC-x"]["C-f"] = reset_search(reset_counter(reset_mark(find_file)))
    keymap_emacs["LC-x"]["C-s"] = reset_search(reset_counter(reset_mark(save_buffer)))
    keymap_emacs["LC-x"]["C-w"] = reset_search(reset_counter(reset_mark(write_file)))
    keymap_emacs["LC-x"]["C-n"] = reset_search(reset_counter(reset_mark(new_buffer)))

    ## 「カーソル移動」のキー設定
    keymap_emacs["LC-b"] = reset_search(reset_counter(repeat(mark(backward_char))))
    keymap_emacs["LC-f"] = reset_search(reset_counter(repeat(mark(forward_char))))

    keymap_emacs["LA-b"]                = reset_search(reset_counter(repeat(mark(backward_word))))
    keymap_emacs["Esc"]["b"]            = reset_search(reset_counter(repeat(mark(backward_word))))
    keymap_emacs["LC-OpenBracket"]["b"] = reset_search(reset_counter(repeat(mark(backward_word))))

    keymap_emacs["LA-f"]                = reset_search(reset_counter(repeat(mark(forward_word))))
    keymap_emacs["Esc"]["f"]            = reset_search(reset_counter(repeat(mark(forward_word))))
    keymap_emacs["LC-OpenBracket"]["f"] = reset_search(reset_counter(repeat(mark(forward_word))))

    keymap_emacs["LC-p"] = reset_search(reset_counter(repeat(mark(previous_line))))
    keymap_emacs["LC-n"] = reset_search(reset_counter(repeat(mark(next_line))))
    keymap_emacs["LC-a"] = reset_search(reset_counter(mark(move_beginning_of_line)))
    keymap_emacs["LC-e"] = reset_search(reset_counter(mark(move_end_of_line)))

    keymap_emacs["LA-S-Comma"]                 = reset_search(reset_counter(mark(beginning_of_buffer)))
    keymap_emacs["Esc"]["S-Comma"]             = reset_search(reset_counter(mark(beginning_of_buffer)))
    keymap_emacs["LC-OpenBracket"]["S-Comma"]  = reset_search(reset_counter(mark(beginning_of_buffer)))

    keymap_emacs["LA-S-Period"]                = reset_search(reset_counter(mark(end_of_buffer)))
    keymap_emacs["Esc"]["S-Period"]            = reset_search(reset_counter(mark(end_of_buffer)))
    keymap_emacs["LC-OpenBracket"]["S-Period"] = reset_search(reset_counter(mark(end_of_buffer)))

    keymap_emacs["LA-v"]                = reset_search(reset_counter(mark(scroll_up)))
    keymap_emacs["Esc"]["v"]            = reset_search(reset_counter(mark(scroll_up)))
    keymap_emacs["LC-OpenBracket"]["v"] = reset_search(reset_counter(mark(scroll_up)))

    keymap_emacs["LC-v"] = reset_search(reset_counter(mark(scroll_down)))

    ## 「カット / コピー / 削除 / アンドゥ」のキー設定
    keymap_emacs["LC-h"]    = reset_search(reset_counter(reset_mark(repeat2(delete_backward_char))))
    keymap_emacs["LC-d"]    = reset_search(reset_counter(reset_mark(repeat2(delete_char))))
    keymap_emacs["LC-Back"] = reset_search(reset_counter(reset_mark(repeat(backward_kill_word))))

    keymap_emacs["LA-Delete"]                = reset_search(reset_counter(reset_mark(repeat(backward_kill_word))))
    keymap_emacs["Esc"]["Delete"]            = reset_search(reset_counter(reset_mark(repeat(backward_kill_word))))
    keymap_emacs["LC-OpenBracket"]["Delete"] = reset_search(reset_counter(reset_mark(repeat(backward_kill_word))))

    keymap_emacs["LC-Delete"] = reset_search(reset_counter(reset_mark(repeat(kill_word))))

    keymap_emacs["LA-d"]                = reset_search(reset_counter(reset_mark(repeat(kill_word))))
    keymap_emacs["Esc"]["d"]            = reset_search(reset_counter(reset_mark(repeat(kill_word))))
    keymap_emacs["LC-OpenBracket"]["d"] = reset_search(reset_counter(reset_mark(repeat(kill_word))))

    keymap_emacs["LC-k"] = reset_search(reset_counter(reset_mark(kill_line2)))
    keymap_emacs["LC-w"] = reset_search(reset_counter(reset_mark(kill_region)))

    keymap_emacs["LA-w"]                = reset_search(reset_counter(reset_mark(kill_ring_save)))
    keymap_emacs["Esc"]["w"]            = reset_search(reset_counter(reset_mark(kill_ring_save)))
    keymap_emacs["LC-OpenBracket"]["w"] = reset_search(reset_counter(reset_mark(kill_ring_save)))

    keymap_emacs["LC-c"]          = reset_search(reset_counter(reset_mark(windows_copy)))
    keymap_emacs["LC-y"]          = reset_search(reset_counter(reset_mark(yank)))
    keymap_emacs["LC-z"]          = reset_search(reset_counter(reset_mark(undo)))
    # keymap_emacs["LC-Slash"]      = reset_search(reset_counter(reset_mark(undo)))
    keymap_emacs["LC-Underscore"] = reset_search(reset_counter(reset_mark(undo)))
    keymap_emacs["LC-x"]["u"]     = reset_search(reset_counter(reset_mark(undo)))

    # LC-Atmark とすると英語キーボードで LC-2 が横取りされるので、LC-(192) としている
    # keymap_emacs["LC-(192)"] = reset_search(reset_counter(set_mark_command))
    keymap_emacs["LC-Space"] = reset_search(reset_counter(set_mark_command))

    keymap_emacs["LC-x"]["h"]   = reset_search(reset_counter(reset_mark(mark_whole_buffer)))
    keymap_emacs["LC-x"]["C-p"] = reset_search(reset_counter(reset_mark(mark_page)))

    ## 「バッファ / ウインドウ操作」のキー設定
    keymap_emacs["LC-x"]["k"] = reset_search(reset_counter(reset_mark(kill_buffer)))
    keymap_emacs["LC-q"] = reset_search(reset_counter(reset_mark(kill_buffer)))
    keymap_emacs["LC-x"]["o"] = reset_search(reset_counter(reset_mark(other_window)))

    ## 「文字列検索 / 置換」のキー設定
    keymap_emacs["LC-r"] = reset_counter(reset_mark(isearch_backward))
    keymap_emacs["LC-s"] = reset_counter(reset_mark(isearch_forward))
    keymap_emacs["LA-x"] = replace

    ## 「その他」のキー設定
    keymap_emacs["LC-m"]        = reset_counter(reset_mark(repeat(newline)))
    keymap_emacs["Enter"]       = reset_counter(reset_mark(repeat(newline)))
    keymap_emacs["LC-j"]        = reset_counter(reset_mark(newline_and_indent))
    keymap_emacs["LC-i"]        = reset_counter(reset_mark(repeat(indent_for_tab_command)))
    keymap_emacs["Tab"]         = reset_counter(reset_mark(repeat(indent_for_tab_command)))
    keymap_emacs["LC-g"]        = reset_search(reset_counter(reset_mark(keybord_quit)))
    keymap_emacs["LC-x"]["C-c"] = reset_search(reset_counter(reset_mark(kill_emacs)))
    keymap_emacs["LC-x"]["C-y"] = reset_search(reset_counter(reset_mark(clipboard_list)))

    ## Excel のキー設定（オプション）
    if 1:
        keymap_excel = keymap.defineWindowKeymap(class_name='EXCEL*')
        # C-Enter 押下で、「セル編集モード」に移行する
        keymap_excel["LC-Enter"] = reset_search(reset_counter(reset_mark(self_insert_command("F2"))))
