import tkinter as T

win = T.Tk()

b = "300"
h = "300"
x = "300"
y = "300"

win.geometry(b + "x" + h + "+" + x + "+" + y)

win.title("this is a title of the window")

b1 = T.Button(text = "exit", width= 10, command = win.destroy )
b1.pack(side="top")
# b1.grid(row = 1, column= 0)

win.mainloop()