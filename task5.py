import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title("Задание №5")
root.geometry("650x400")
my_font = ctk.CTkFont(family="Roboto", size=20)


rows, columns = 5, 3
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    if i == 0:
        root.columnconfigure(index=i, weight=2)
    else:
        root.columnconfigure(index=i, weight=1)

label = ctk.CTkLabel(master=root)
label.configure(
    text="Добавьте товар",
    font=my_font,
    text_color="white"
)

label_2 = ctk.CTkLabel(master=root)
label_2.configure(
    text="Суть:",
    font=my_font,
    text_color="white"
)

label_3 = ctk.CTkLabel(master=root)
label_3.configure(
    text="Категория товара:",
    font=my_font,
    text_color="white"
)

btn_1 = ctk.CTkButton(master=root, text="Вернуться", font=my_font)
btn_2 = ctk.CTkButton(master=root, text="Добавить", font=my_font)

entry = ctk.CTkEntry(master=root)
entry.configure(
    placeholder_text="Название",
    justify="center",
    font=my_font,
    width=200,
    height=50
)

entry_2 = ctk.CTkEntry(master=root)
entry_2.configure(
    placeholder_text="Цена",
    justify="center",
    font=my_font,
    width=200,
    height=50
)

elems = ["Еда", "Транспорт", "Одежда", "Быт. товары", "Лекарства", "Крупные траты"]
combobox = ctk.CTkComboBox(master=root)
combobox.configure(
    font=my_font,
    values=elems,
    state="readonly",
    width=300
)
combobox.set("Еда")

label.grid(row=0, column=0, columnspan=3)
label_2.grid(row=1, column=0)
label_3.grid(row=2, column=0)
btn_1.grid(row=3, column=0)
btn_2.grid(row=4, column=0)
entry.grid(row=1, column=1)
entry_2.grid(row=1, column=2)
combobox.grid(row=2, column=1, columnspan=2)

root.mainloop()
