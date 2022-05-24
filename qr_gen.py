from tkinter import *
import pyqrcode
from PIL import ImageTk, Image

root = Tk()

canvas = Canvas(root, width=400, height=600)
canvas.pack()

app_label = Label(root, text="QR Code Generator", fg='blue', font=("Arial", 30))
canvas.create_window(200, 50, window=app_label)

root.mainloop()

