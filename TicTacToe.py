import tkinter as tk
from tkinter import messagebox

graph = [""]*9
x = "X"
game_over = False

win_index = [
    [0,1,2],[3,4,5],[6,7,8],
    [0,3,6],[1,4,7],[2,5,8],
    [0,4,8],[2,4,6]
]

root = tk.Tk()
root.title("Tic-Tac-Toe")
root.geometry("400x350")
display = tk.StringVar()

label = tk.Label(root,textvariable=display,font=("Arial",15))
label.grid(row=3,column=0,columnspan=3,pady=10)

buttons = []
display.set("X's Turn")
for i in range(9):
    btn = tk.Button(
        root,
        text= "",
        font="Arial,30",
        width= 10,
        height=3,
        command=lambda i=i:after_click(i),
        fg="White",
        bg = "Black",
    )
    btn.config(padx=10,pady=10)
    btn.grid(row=i//3,column=i%3)
    buttons.append(btn)

def winner_check():
    for win in win_index:
        a,b,c = win
        if graph[a] == graph[b] ==  graph[c] != "":
            return True
    return False
    
def after_click(index):
    global x,game_over

    if graph[index] != "" or game_over:
        return
    
    graph[index] = x
    buttons[index].config(
        text= x
    )

    if winner_check():
        messagebox.showinfo("showinfo",f"{x} won!")
        game_over = True
    elif "" not in graph:
        messagebox.showinfo("showinfo","It's a tie")
        game_over = True
    else:
        x = "O" if x == "X" else "X"
        display.set(f"{x}'s Turn")
        
def reset():
    global x, graph, game_over
    graph = [""]*9
    x = "X"
    game_over = False
    for btn in buttons:
        btn.config(text = "")
    display.set(f"{x}'s Turn!")

tk.Button(root, text="Restart", command=reset).grid(row=4, column=0, columnspan=3)

root.mainloop()