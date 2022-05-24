from tkinter import *
import pyqrcode
from PIL import ImageTk, Image

root = Tk()

canvas = Canvas(root, width=400, height=600)
canvas.pack()

app_label = Label(root, text="QR Code Generator", fg='blue', font=("Arial", 30))
canvas.create_window(200, 50, window=app_label)

name_label = Label(root, text="Link name")
canvas.create_window(200, 100, window=name_label)
link_label = Label(root, text="Link")
canvas.create_window(200, 160, window=link_label)

name_entry = Entry(root)
canvas.create_window(200, 130, window=name_entry)
link_entry = Entry(root)
canvas.create_window(200, 180, window=link_entry)

root.mainloop()

