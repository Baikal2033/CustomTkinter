import customtkinter as ctk


def handle_button_press(chosen_elem):
    text = chosen_elem
    entry.configure(state="normal")  # разблокируем поле
    entry.delete(0, "end")  # удалим оттуда старую строчку
    entry.insert(0, text)  # вставим новую
    entry.configure(state="readonly")  # снова заблокируем

def handle_combobox_choice(chosen_elem):  # хендлер для ComboBox должен принимать один аргумент - выбранный элемент
    # он срабатывает, когда мы выбираем в выпадающем списке какой-то элемент
    print(f"Выбранный элемент: {chosen_elem}")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title("Задание №3")
root.geometry("500x500")
my_font = ctk.CTkFont(family="Roboto", size=20)

entry = ctk.CTkEntry(master=root)
entry.configure(
    justify="center",
    font=my_font,
    width=250
)
entry.insert(0, "")  # вставили в поле текст
entry.configure(state="readonly")  # заблокировали поле

# RadioButton - переключатели:
# образуют связанную группу - когда включён один переключатель, выключены другие
var_radiobuttons = ctk.IntVar()  # переключатели будут привязаны к одной переменной типа int, образуя связанную группу

radiobutton_1 = ctk.CTkRadioButton(
    master=root,
    variable=var_radiobuttons,  # привязываем переключатель к переменной
    value=1  # значение данного переключателя
)
# параметры variable и value обязательно указываем при создании, а не в .configure()
radiobutton_1.configure(text="Белый цвет текста", font=my_font)

radiobutton_2 = ctk.CTkRadioButton(master=root, variable=var_radiobuttons, value=2)
radiobutton_2.configure(text="Красный цвет текста", font=my_font)
radiobutton_3 = ctk.CTkRadioButton(master=root, variable=var_radiobuttons, value=3)
radiobutton_3.configure(text="Жёлтый цвет текста", font=my_font)

var_radiobuttons.set(1)  # значение переменной по умолчанию, то есть по умолчанию будет активен 1-ый переключатель

# взаимодействие с RadioButton:
var_radiobuttons.get()  # получаем текущее значение переменной, если 1 => включён первый переключатель, иначе - второй

# ComboBox - выпадающий список для выбора одного элемента
elems = ["Ты уходишь", "Ты спишь", "Ты работаешь"]  # список элементов
combobox = ctk.CTkComboBox(master=root)
combobox.configure(
    font=my_font,
    values=elems,  # указываем созданный ранее список элементов
    state="readonly",  # режим "только для чтения", чтобы пользователь не мог случайно стереть выбираемый элемент
    width=250
)
combobox.set("Выберите фразу:")  # значение элемента по умолчанию
combobox.configure(command=handle_combobox_choice)

# взаимодействие с ComboBox:
combobox.get()  # получить выбранное значение

var_checkbox_1 = ctk.BooleanVar()  # первый флажок будет привязан к первой переменной
# она имеет тип bool, то есть может принимать всего два значения: True или False; это логично, потому что флажок тоже
# может принимать всего два состояния: активен или не активен; свяжем состояние "активен" с True, "не активен" - с False

checkbox_1 = ctk.CTkCheckBox(
    master=root,
    variable=var_checkbox_1,  # переменная, к которой привязываем флажок
    onvalue=True,  # значение переменной, когда флажок активен, мы решили, что это будет True
    offvalue=False  # значение переменной, когда флажок не активен, мы решили, что это будет False
)
checkbox_1.configure(text="Добавить в конец !", font=my_font)

var_checkbox_1.set(True)  # значение переменной по умолчанию, то есть по умолчанию первый флажок будет активен

var_checkbox_2 = ctk.BooleanVar()  # второй флажок будет привязан ко второй переменной
checkbox_2 = ctk.CTkCheckBox(master=root, variable=var_checkbox_2, onvalue=True, offvalue=False)
checkbox_2.configure(text="Добавить в конец ?", font=my_font)
var_checkbox_2.set(False)  # значение переменной по умолчанию, то есть по умолчанию второй флажок будет неактивен

# взаимодействие с CheckBox:
var_checkbox_1.get()  # True или False
var_checkbox_2.get()


button = ctk.CTkButton(master=root, text="Выбрать", font=my_font, command=handle_button_press)

entry.pack(pady=15)
radiobutton_1.pack(pady=15)
radiobutton_2.pack(pady=15)
radiobutton_3.pack(pady=15)
combobox.pack(pady=15)
checkbox_1.pack(pady=15)
checkbox_2.pack(pady=15)
button.pack(pady=15)

root.mainloop()
