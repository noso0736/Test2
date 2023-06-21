import tkinter as tk

root=tk.Tk()
root.geometry("500x500")

canvas=tk.Canvas(root,bg="white")

canvas.pack(fill=tk.BOTH,expand=True)

m=canvas.create_oval(150,70,220,140)
m1=canvas.create_line(185,140,185,250)
m2=canvas.create_line(185,180,235,140)
m3=canvas.create_line(185,180,135,140)
m4=canvas.create_line(185,250,235,300)
m5=canvas.create_line(185,250,135,300)

def move():
 canvas.move(m,10,0)
 canvas.move(m1,10,0)
 canvas.move(m2,10,0)
 canvas.move(m3,10,0)
 canvas.move(m4,10,0)
 canvas.move(m5,10,0)
 canvas.after(100,move)

def clk():
    move()
button = tk.Button(root, text="押せ", command=clk)
button.pack()

root.mainloop()