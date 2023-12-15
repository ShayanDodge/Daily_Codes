import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame(master=window, width=500, height=100, bg="red")
frame1.pack()

frame2 = tk.Frame(master=window, width=500, height=100, bg="yellow")
frame2.pack()

frame3 = tk.Frame(master=window, width=500, height=100, bg="blue")
frame3.pack()

window.mainloop()