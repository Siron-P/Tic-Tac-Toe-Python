import tkinter as tk 

graph = [""]*9
x = "X"
game_over = False

root = tk.Tk()
root.title("Tic-Tac-Toe")
root.geometry("400x300")

for i in range(9):
    btn = tk.Button(
        root,
        text= "",
        font="Arial",
        width= 10,
        height=3,
        bg= "Black"
    )
    btn.config(
        
        padx=10,
        pady=10
    )
    btn.grid(row=i//3,column=i%3)

root.mainloop()