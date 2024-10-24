from tkinter import *
def change_red():
    color_code_entry.delete(0, END)
    color_code_entry.insert(0, "#ff0000")
    color_label.config(text="Красный")
    
    color_label = Label(root, text="", font=("Arial", 12))


color_code_entry = Entry(root, justify=CENTER)
color_code_entry.pack()
