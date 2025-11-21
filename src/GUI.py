import tkinter as tk
from tkinter import *

# 메인 윈도우 생성
window = tk.Tk()
window.title("MineSweeper")
window.geometry("1280x690+200+200")
window.resizable(False, False)

# 메인 배경색 (그라데이션 느낌을 위해 약한 연보라색)
MAIN_BG = "#d7d6f5"    # 연한 퍼플+블루톤
PANEL_BG = "#ffffff"   # 우측 패널은 하얀 상자 느낌
BOARD_BG = "#e9e7fb"   # 보드 영역 흐린 라벤더
PAD_BG = "#d7d6f5"     # 패딩 프레임 동일 색

window.configure(bg=MAIN_BG)

# UI 전체 프레임
main = tk.Frame(window, bg=MAIN_BG)
main.pack(fill="both", expand=True)

# 상단 패딩
center_northPadding = tk.Frame(main, height=20, bg=MAIN_BG)
center_northPadding.pack(fill="x")

# 중앙 영역 전체
center_panel = tk.Frame(main, bg=MAIN_BG)
center_panel.pack(fill="both", expand=True)

# 좌측 패딩
left_padding = tk.Frame(center_panel, width=20, bg=MAIN_BG)
left_padding.pack(side="left", fill="y")

# 보드 바깥 영역
board_outer = tk.Frame(center_panel, width=860, height=645, bg=MAIN_BG)
board_outer.pack(side="left", anchor="nw")

# 보드 내부(버튼 들어가는 공간)
board_inner = tk.Frame(board_outer, bg=BOARD_BG)
board_inner.place(x=10, y=10, width=840, height=630)

# 가운데 패딩
mid_padding = tk.Frame(center_panel, width=20, bg=MAIN_BG)
mid_padding.pack(side="left", fill="y")

# 우측 정보 패널
right_panel = tk.Frame(center_panel, width=360, height=645, 
                       bg=PANEL_BG, highlightthickness=0)
right_panel.pack(side="left", anchor="nw")
right_panel.pack_propagate(False)

# 우측 패널 타이틀
right_panel_title = tk.Label(
    right_panel, text="지뢰 찾기",
    font=("Arial", 30, "bold"),
    bg=PANEL_BG, fg="#222"
)
right_panel_title.pack(side="top", fill="x", pady=10)

# 남은 시간
time_left = tk.Label(
    right_panel, text="00:00",
    font=("Arial", 50, "bold"),
    bg=PANEL_BG, fg="#111"
)
time_left.pack(side="top", fill="x")

# 남은 지뢰 수
left_mine = tk.Label(
    right_panel, text="남은 지뢰 : 5개",
    font=("Arial", 25, "bold"),
    bg=PANEL_BG, fg="#222"
)
left_mine.pack(side="top", fill="x")

# BUTTONS
COL = 20
ROW = 15

def clickButton(i, j):
    print(i, j)


nullImg = PhotoImage(file = "src/resources/normal.png")
flagImg = PhotoImage(file = "src/resources/flag.png")
window.tk.call('tk','scaling',1.0)
buttons = []
for i in range(ROW):
    row = []
    for j in range(COL):
        button = tk.Button(
            board_inner,
            image=nullImg,
            borderwidth=1,
            command=lambda i=i, j=j: clickButton(i, j)
        )
        button.grid(row=i, column=j)
        row.append(button)
    buttons.append(row)

# 메뉴 바
def exitGame():
    window.quit()
    window.destroy()

menubar = Menu(window)
opt = Menu(menubar, tearoff=0)
opt.add_command(label="새 게임")
opt.add_command(label="다시 시작")
opt.add_separator()
opt.add_command(label="게임 종료", command=exitGame)
menubar.add_cascade(label="Menu", menu=opt)
window.config(menu=menubar)

window.mainloop()
