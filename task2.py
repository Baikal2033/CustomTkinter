import customtkinter as ctk


def handle_button_press():
    global root, entry, entry_two, entry_three
    text = int(entry.get())  # получаем введённую в поле строку в типе str
    text_two = int(entry_two.get())  # получаем введённую в поле строку в типе str

    text_three = text + text_two
    entry_three.configure(state="normal")  # разблокируем поле
    entry_three.delete(0, "end")  # удалим оттуда старую строчку
    entry_three.insert(0, text_three)  # вставим новую
    entry_three.configure(state="readonly")


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title("Задача №2")
root.geometry("500x500")
my_font = ctk.CTkFont(size=20)


entry = ctk.CTkEntry(master=root)
entry.configure(
    placeholder_text="",
    justify="center",
    font=my_font,
    width=250
)

entry_two = ctk.CTkEntry(master=root)
entry_two.configure(
    placeholder_text="",
    justify="center",
    font=my_font,
    width=250
)

entry_three = ctk.CTkEntry(master=root)
entry_three.configure(
    justify="center",
    font=my_font,
    width=250
)
entry_three.insert(0, "")
entry_three.configure(state="readonly")

label = ctk.CTkLabel(master=root)
label.configure(
    text="+",
    font=my_font,
    text_color="white"
)

label_two = ctk.CTkLabel(master=root)
label_two.configure(
    text="=",
    font=my_font,
    text_color="white"
)

button = ctk.CTkButton(master=root, text="Посчитать", font=my_font, command=handle_button_press)

entry.pack(pady=20)
label.pack(pady=20)
entry_two.pack(pady=20)
label_two.pack(pady=20)
entry_three.pack(pady=20)
button.pack(pady=20)

root.mainloop()
