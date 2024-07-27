import tkinter as tk
import time
import math
 
 # tk.Frameを継承したApplicationクラスを作成
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
 
        # ウィンドウの設定
        master.title("東ポモドーロ")
        master.geometry("710x280") # タイマーの幅は430x280
 
        # 変数定義
        self.timer_on = False # タイマーの状態
        self.start_time = 0 # 開始時間
        self.set_time = 0 # セット時間
        self.elapsed_time = 0 # 経過時間
        self.left_time = 0 # 残り時間
        self.left_min = 0 # 残り時間（分）
        self.left_sec = 0 # 残り時間（秒）
        self.after_id = 0 # after_id変数を定義
 
        # 実行内容
        self.pack()
        self.create_widget()
 
    # create_widgetメソッドを定義
    def create_widget(self):
 
        # 全体の親キャンバス
        self.canvas_bg = tk.Canvas(self.master, width=800, height=280)
        self.canvas_bg.pack()
 
        # タイマー用のキャンバス
        self.canvas_time = tk.Canvas(self.canvas_bg, width=690, height=80, bg="lightgreen")
        self.canvas_time.place(x=10, y=10)
 
        # タイマーに数字を表示
        self.update_min_text() # 分の表示更新
        self.update_sec_text() # 秒の表示更新
 
        # 10分ボタン
        self.min_button = tk.Button(self.canvas_bg, width=8, height=2, text="10分", font=("MSゴシック体", "18","bold"), command=self.ten_min_button_clicked)
        self.min_button.place(x=10, y=100)

        # 1分ボタン
        self.min_button = tk.Button(self.canvas_bg, width=8, height=2, text="1分", font=("MSゴシック体", "18","bold"), command=self.one_min_button_clicked)
        self.min_button.place(x=150, y=100)
 
        # 10秒ボタン
        self.sec_button = tk.Button(self.canvas_bg, width=8, height=2, text="10秒", font=("MSゴシック体", "18","bold"), command=self.ten_sec_button_clicked)
        self.sec_button.place(x=290, y=100)

        # 1秒ボタン
        self.sec_button = tk.Button(self.canvas_bg, width=8, height=2, text="1秒", font=("MSゴシック体", "18","bold"), command=self.one_sec_button_clicked)
        self.sec_button.place(x=430, y=100)
 
        # リセットボタン
        self.reset_button = tk.Button(self.canvas_bg, width=8, height=2, text="リセット", font=("MSゴシック体", "18","bold"), command=self.reset_button_clicked)
        self.reset_button.place(x=570, y=100)
 
        # スタート/ストップボタン
        start_button = tk.Button(self.canvas_bg, width=27, height=2, text="スタート/ストップ", font=("MSゴシック体", "18","bold"), command=self.start_button_clicked)
        start_button.place(x=150, y=190)
 
# 各ボタンを押した時の処理
 
    # 1分ボタンを押した時
    def one_min_button_clicked(self):
        if self.left_min < 59: # 最大59分まで
            self.set_time += 60 # セット時間をプラス
            self.left_min += 1 # 残り時間（分）をプラス
            self.update_min_text() # 分の表示更新
    
    # 10分ボタンを押した時
    def ten_min_button_clicked(self):
        if self.left_min < 59: # 最大59分まで
            self.set_time += 600 # セット時間をプラス
            self.left_min += 10 # 残り時間（分）をプラス
            self.update_min_text() # 分の表示更新
 
    # 1秒ボタンを押した時
    def one_sec_button_clicked(self):
        if self.left_sec < 59: # 最大59秒まで
            self.set_time += 1 # セット時間をプラス
            self.left_sec += 1 # 残り時間（秒）をプラス
            self.update_sec_text() # 秒の表示更新
    
     # 10秒ボタンを押した時
    def ten_sec_button_clicked(self):
        if self.left_sec < 59: # 最大59秒まで
            self.set_time += 10 # セット時間をプラス
            self.left_sec += 10 # 残り時間（秒）をプラス
            self.update_sec_text() # 秒の表示更新
 
    # resetボタンを押した時
    def reset_button_clicked(self):
        self.set_time = 0 # セット時間をリセット
        self.left_min = 0 # 残り時間（分）をリセット
        self.left_sec = 0 # 残り時間（秒）をリセット
 
        self.update_min_text() # 分の表示更新
        self.update_sec_text() # 秒の表示更新
 
    #startボタンを押した時
    def start_button_clicked(self):
 
        if self.set_time >= 1:
 
            if self.timer_on == False:
                self.timer_on = True
 
                # 各種ボタンを押せなくする
                self.min_button["state"] = tk.DISABLED
                self.sec_button["state"] = tk.DISABLED
                self.reset_button["state"] = tk.DISABLED
 
                self.start_time =time.time() # 開始時間を代入
                self.update_time() # updateTime関数を実行
 
            elif self.timer_on == True:
                self.timer_on = False
 
                # 各種ボタンを押せるようにする
                self.min_button["state"] = tk.NORMAL
                self.sec_button["state"] = tk.NORMAL
                self.reset_button["state"] = tk.NORMAL
 
                self.set_time = self.left_time
                app.after_cancel(self.after_id)
 
# 個別の処理
 
    # 時間更新処理
    def update_time(self):
        self.elapsed_time = time.time() - self.start_time  # 経過時間を計算
        self.left_time = self.set_time - self.elapsed_time # 残り時間を計算
        self.left_min = math.floor(self.left_time // 60) # 残り時間（分）を計算
        self.left_sec = math.floor(self.left_time % 60) # 残り時間（秒）を計算
 
        self.update_min_text() # 分の表示更新
        self.update_sec_text() # 秒の表示更新
 
        if self.left_time > 0.1:
            self.after_id = self.after(10, self.update_time)
        else:
            self.timer_on = False
 
            # 各種ボタンを押せるようにする
            self.min_button["state"] = tk.NORMAL
            self.sec_button["state"] = tk.NORMAL
            self.reset_button["state"] = tk.NORMAL
 
            self.set_time = self.left_time
            app.after_cancel(self.after_id)
 
    # 分の表示更新
    def update_min_text(self):
        self.canvas_time.delete("min_text") # 表示時間（分）を消去
        self.canvas_time.create_text(365, 40, text=str(self.left_min).zfill(2) + "：", font=("MSゴシック体", "36", "bold"), tag="min_text", anchor="e") # 分を表示
 
    # 秒の表示更新
    def update_sec_text(self):
        self.canvas_time.delete("sec_text") # 表示時間（秒）を消去
        self.canvas_time.create_text(365,40,text=str(self.left_sec).zfill(2), font=("MSゴシック体", "36", "bold"), tag="sec_text", anchor="w") # 秒を表示
 
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()