from tkinter import *

t = Tk()
t.title("Transparency")

frame = Frame(t)
frame.pack()

canvas = Canvas(frame, bg="black", width=500, height=500)
canvas.pack()

photoimage = PhotoImage(file="images/white.gif")
canvas.create_image(150, 150, image=photoimage)

t.mainloop()
