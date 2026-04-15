import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Задание №5.1")
root.geometry("650x400")
my_font = ctk.CTkFont(family="Roboto", size=20)

elems = ["Элемент 1", "Элемент 2", "Элемент 3"]  # список элементов
combobox = ctk.CTkComboBox(master=root)
combobox.configure(
    font=my_font,
    values=elems,
    state="readonly",
    width=250
)
combobox.set("Выберите тип шифрования")

# взаимодействие с ComboBox:
combobox.get()  # получить выбранное значение

elems_2 = ["Элемент 1", "Элемент 2", "Элемент 3"]  # список элементов
combobox_2 = ctk.CTkComboBox(master=root)
combobox_2.configure(
    font=my_font,
    values=elems,
    state="readonly",
    width=250
)
combobox_2.set("Шифрование")

# взаимодействие с ComboBox:
combobox_2.get()  # получить выбранное значение

elems_3 = ["Элемент 1", "Элемент 2", "Элемент 3"]  # список элементов
combobox_3 = ctk.CTkComboBox(master=root)
combobox_3.configure(
    font=my_font,
    values=elems,
    state="readonly",
    width=250
)
combobox_3.set("Русский язык")

# взаимодействие с ComboBox:
combobox_3.get()  # получить выбранное значение

textbox = ctk.CTkTextbox(master=root)
textbox.configure(font=my_font, height=150, width=600)

textbox_2 = ctk.CTkTextbox(master=root)
textbox_2.configure(font=my_font, height=200, width=350)

button = ctk.CTkButton(master=root, text="Готово", font=my_font, width=300)

rows, columns = 6, 2
for i in range(rows):
    if i == 5:
        root.rowconfigure(index=i, weight=3)
    else:
        root.rowconfigure(index=i, weight=1)

for i in range(columns):
    if i == 1:
        root.columnconfigure(index=i, weight=2)
    else:
        root.columnconfigure(index=i, weight=1)


combobox.grid(row=0, column=0)
combobox_2.grid(row=2, column=0)
combobox_3.grid(row=3, column=0)
textbox.grid(row=5, column=0, columnspan=2)
textbox_2.grid(row=0, column=1, rowspan=4)
button.grid(row=4, column=1)

root.mainloop()
