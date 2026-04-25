import time

import customtkinter as ctk
from PIL import Image
from customtkinter import CTkLabel


def handler(i, j):
    global score, matrix_steps, flag
    if matrix_steps[i][j] == 0 and flag:
        if score == 1:
            matrix_lbls[i][j].configure(image=image_ctk_utility_krest)
            matrix_steps[i][j] = 1
            score = 2
        elif score == 2:
            matrix_lbls[i][j].configure(image=image_ctk_utility_nolik)
            score = 1
            matrix_steps[i][j] = 2
    if matrix_steps[0][2] == matrix_steps[1][1] == matrix_steps[2][0] != 0:
        if matrix_steps[0][2] == 1:
            label.configure(text="Крестики выиграли")
        if matrix_steps[0][2] == 2:
            label.configure(text="Нолики выиграли")
        flag = False
    if matrix_steps[0][0] == matrix_steps[1][1] == matrix_steps[2][2] != 0:
        if matrix_steps[0][0] == 1:
            label.configure(text="Крестики выиграли")
        if matrix_steps[0][0] == 2:
            label.configure(text="Нолики выиграли")
        flag = False
    if matrix_steps[0][0] == matrix_steps[1][0] == matrix_steps[2][0] != 0:
        if matrix_steps[0][0] == 1:
            label.configure(text="Крестики выиграли")
        if matrix_steps[0][0] == 2:
            label.configure(text="Нолики выиграли")
        flag = False
    if matrix_steps[0][1] == matrix_steps[1][1] == matrix_steps[2][1] != 0:
        if matrix_steps[0][1] == 1:
            label.configure(text="Крестики выиграли")
        if matrix_steps[0][1] == 2:
            label.configure(text="Нолики выиграли")
        flag = False
    if matrix_steps[0][2] == matrix_steps[1][2] == matrix_steps[2][2] != 0:
        if matrix_steps[0][2] == 1:
            label.configure(text="Крестики выиграли")
        if matrix_steps[0][2] == 2:
            label.configure(text="Нолики выиграли")
        flag = False
    if matrix_steps[0][0] == matrix_steps[0][1] == matrix_steps[0][2] != 0:
        if matrix_steps[0][0] == 1:
            label.configure(text="Крестики выиграли")
        if matrix_steps[0][0] == 2:
            label.configure(text="Нолики выиграли")
        flag = False
    if matrix_steps[1][0] == matrix_steps[1][1] == matrix_steps[1][2] != 0:
        if matrix_steps[1][0] == 1:
            label.configure(text="Крестики выиграли")
        if matrix_steps[1][0] == 2:
            label.configure(text="Нолики выиграли")
        flag = False
    if matrix_steps[2][0] == matrix_steps[2][1] == matrix_steps[2][2] != 0:
        if matrix_steps[2][0] == 1:
            label.configure(text="Крестики выиграли")
        if matrix_steps[2][0] == 2:
            label.configure(text="Нолики выиграли")
        flag = False
    if flag:
        flag_matrix = True  # считаем изначально, что в матрице нет 0
        for i in range(3):
            for j in range(3):
                if matrix_steps[i][j] == 0:
                    flag_matrix = False
                    break
        if flag_matrix:
            label.configure(text="Ничья")




ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title("Задание №7")
root.geometry("500x500")
my_font = ctk.CTkFont(family="Roboto", size=20)

# работа с изображением:
image_object_fon = Image.open("images/fon.png")
image_ctk_utility_fon = ctk.CTkImage(dark_image=image_object_fon, size=(120, 120))

image_object_krest = Image.open("images/krest.png")
image_ctk_utility_krest = ctk.CTkImage(dark_image=image_object_krest, size=(120, 120))

image_object_nolik = Image.open("images/nolik.png")
image_ctk_utility_nolik = ctk.CTkImage(dark_image=image_object_nolik, size=(120, 120))

# рамка для плитки
frame = ctk.CTkFrame(master=root)

label = ctk.CTkLabel(master=root)
label.configure(
    text="Игра продолжается",
    font=my_font,
    text_color="white"
)

flag = True

# внешняя сетка для окна root:
rows, columns = 2, 1
for i in range(rows):
    if i == 1:
        root.rowconfigure(index=i, weight=5)
    else:
        root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)
frame.grid(row=0, column=0)
label.grid(row=1, column=0)

# внутри рамки frame будет плитка из labels 2x3:

# создание хендлеров для labels:
matrix_handlers = []
for i in range(3):
    tmp_lst = []
    for j in range(3):
        handler_ij = lambda x, i_actual=i, j_actual=j: handler(i_actual, j_actual)
        # параметр x был нужен, так как при привязке хендлера к Label
        # обязательно должен быть один принимающий значение параметр, хоть он нам и не понадобится
        tmp_lst.append(handler_ij)
    matrix_handlers.append(tmp_lst)

# создание виджетов labels и привязка к ним изображений и хендлеров:
matrix_lbls = []
for i in range(3):
    tmp_lst = []
    for j in range(3):
        lbl_ij = ctk.CTkLabel(master=frame, text="", image=image_ctk_utility_fon)
        lbl_ij.bind("<Button-1>", matrix_handlers[i][j])
        lbl_ij.configure(cursor="hand2")
        tmp_lst.append(lbl_ij)
    matrix_lbls.append(tmp_lst)

matrix_steps = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# внутренняя сетка для рамки frame:
rows, columns = 3, 3
for i in range(rows):
    frame.rowconfigure(index=i, weight=1)
for i in range(columns):
    frame.columnconfigure(index=i, weight=1)
for i in range(3):
    for j in range(3):
        lbl_ij = matrix_lbls[i][j]
        lbl_ij.grid(row=i, column=j, padx=5, pady=5)  # сделаем небольшие отступы между картинками

score = 1  # 1 - krest, 2 - nolik
steps = set()

root.mainloop()
