import tkinter as tk

root=tk.Tk()
root.geometry("500x500")

canvas=tk.Canvas(root,bg="white")

canvas.pack(fill=tk.BOTH,expand=True)

canvas.create_oval(150,70,220,140)
canvas.create_line(185,140,185,250)
canvas.create_line(185,180,235,140)
canvas.create_line(185,180,135,140)
canvas.create_line(185,250,235,300)
canvas.create_line(185,250,135,300)
root.mainloop()