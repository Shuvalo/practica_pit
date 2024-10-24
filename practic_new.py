from tkinter import *
def change_red():
    color_code_entry.delete(0, END)
    color_code_entry.insert(0, "#ff0000")
    color_label.config(text="Красный")

def change_orange():
    color_code_entry.delete(0, END)
    color_code_entry.insert(0, "#ff7d00")
    color_label.config(text="Оранжевый")

def change_yellow():
    color_code_entry.delete(0, END)
    color_code_entry.insert(0, "#ffff00")
    color_label.config(text="Желтый")

def change_green():
    color_code_entry.delete(0, END)
    color_code_entry.insert(0, "#00ff00")
    color_label.config(text="Зеленый")

def change_blue():
    color_code_entry.delete(0, END)
    color_code_entry.insert(0, "#0000ff")
    color_label.config(text="Синий")

def change_indigo():
    color_code_entry.delete(0, END)
    color_code_entry.insert(0, "#7d00ff")
    color_label.config(text="Красный")

root = Tk()

color_label = Label(root, text="", font=("Arial", 12))


color_code_entry = Entry(root, justify=CENTER)
color_code_entry.pack()

red_button = Button(root, text="Красный", bg="#ff0000", command=change_red)
red_button.pack()

orange_button = Button(root, text="Оранжевый", bg="#ff7d00", command=change_orange)
orange_button.pack()

yellow_button = Button(root, text="Желтый", bg="#ffff00", command=change_yellow)
yellow_button.pack()

green_button = Button(root, text="Зеленый", bg="#00ff00", command=change_green)
green_button.pack()

blue_button = Button(root, text="Синий", bg="#0000ff", command=change_blue)
blue_button.pack()

indigo_button = Button(root, text="Фиолетовый", bg="#7d00ff", command=change_indigo)
indigo_button.pack()

root.mainloop()
