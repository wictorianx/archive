from tkinter import *
import json

root = Tk()
root.geometry("500x300")

kutu = Listbox(root, bg="black", fg="green", width = 60)
kutu.pack()
def ekle(x,kutu):
    kutu.insert(END,x)
    
e = Entry(root, width = 60)
e.pack()
e.insert(0,"gözlem giriniz : ")
def submit():
    global kutu
    ekle(e.get(),kutu)
buton = Button(root, text = "Onayla", command = submit)
buton.pack()