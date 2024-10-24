from tkinter import *
def change_red():
    color_code_entry.delete(0, END)
    color_code_entry.insert(0, "#ff0000")
    color_label.config(text="Красный")