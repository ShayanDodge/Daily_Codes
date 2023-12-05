import tkinter as T

win = T.Tk()

win.geometry("800x600+200+100")

win.title("This is the title of our window")

l1 = T.Label(text = "label1")
l1.pack(side="left")

b1=T.Button(text="Exit", width= 15, command = win.destroy)
b1.pack(side="bottom")

E1 = T.Entry(width=20)
E1.pack(side="top")

E2 = T.Entry(width=20)
E2.pack(side="top")

def addition():
    v1 = int(E1.get())
    v2 = int(E2.get())
    l2 = T.Label(text =  str(v1 + v2))
    l2.pack(side="top")
    E1.delete(0,"end")
    E2.delete(0, "end")

b2=T.Button(text="Addition", width= 15, command = addition)
b2.pack(side="top")

win.mainloop()