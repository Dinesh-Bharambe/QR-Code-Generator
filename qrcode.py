from tkinter import *
from tkinter import messagebox
import pyqrcode
window = Tk()
window.geometry("500x400")
window.title("QR Code Generator")

def generate():    
    if len(e.get()) != 0:
        global qr
        qr = pyqrcode.create(e.get())
        qrimg = qr.xbm(scale = 6)
        global img
        img = BitmapImage(data = qrimg)
        messagebox.showinfo("successful","QR Code Generated Successfully.")
    else:
        messagebox.showinfo("Error","Please enter the url")

def display():
    global img
    l2.config(image = img)

l1 = Label(window,text = "Enter a url",font = ("Ariel",12)).grid(row = 1,column = 0)

e = StringVar()
e1 = Entry(window, textvariable = e,font = ("Ariel",12)).grid(row=1, column=1)

b1 = Button(window, text="Generate QR Code", command=generate).grid(row = 2,column = 0)
b2 = Button(window, text="Display", command=display).grid(row = 2,column = 1)

l2= Label(window)
l2.grid(row= 3, column=1)
window.mainloop()
