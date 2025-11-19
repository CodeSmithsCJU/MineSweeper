import tkinter as tk
import tkinter.font

#Tk객체 생성
window = tk.Tk()

#최상위 윈도우 설정
window.title("MineSweeper")
window.geometry("1280x720+200+200")
window.resizable(False,False)

#Frame 나누기
main = tk.Frame(window,bg="#ddd")
main.pack(fill="both",expand=True)

#상단
option_bar = tk.Frame(main,height=35,bg="gray")
option_bar.pack(fill="x")

#상단 패딩, 좌측 패딩
center_northPadding = tk.Frame(main,height=20,bg="yellow")
center_northPadding.pack(fill="x")

#좌측+우측
center_panel = tk.Frame(main, bg="#ddd")
center_panel.pack(fill="both",expand=True)

left_padding = tk.Frame(center_panel,width=20,bg="yellow")
left_padding.pack(side="left",fill="y")

board_outer = tk.Frame(center_panel,width=860,height=645,bg="black")
board_outer.pack(side="left",anchor="nw")

board_inner = tk.Frame(board_outer,bg="gray")
board_inner.place(x=10,y=10,width=840,height=630)

mid_padding = tk.Frame(center_panel,width=20,bg="yellow")
mid_padding.pack(side="left",fill="y")

right_panel = tk.Frame(center_panel,width=360,height=645,bg="white")
right_panel.pack(side="left",anchor="nw")
right_panel.pack_propagate(False)

right_panel_title = tk.Label(right_panel,text="지뢰 찾기", font=("Arial",30,"bold"),anchor="center")
right_panel_title.pack(side="top", fill="x", pady=10)

time_left = tk.Label(right_panel,text="00:00",font=("Arial",50,"bold"),anchor="center")
time_left.pack(side="top",fill="x")

left_mine = tk.Label(right_panel,text="남은 지뢰 : 5개",font=("Arial",25,"bold"),anchor="center")
left_mine.pack(side="top",fill="x")

#BUTTON
COL = 20
ROW = 15


#버튼 클릭 시 호출
def clickButton(i,j):
    return i,j

#버튼 생성
nullImg = tk.PhotoImage(width=36,height=36)
buttons = []
for i in range(ROW):
    row = []
    for j in range(COL):
        button = tk.Button(
            board_inner,
            image=nullImg,
            command=lambda i=i, j=j: clickButton(i,j))
        button.grid(row=i,column=j)
        row.append(button)
    buttons.append(row)


#윈도우 지속시키기
window.mainloop()