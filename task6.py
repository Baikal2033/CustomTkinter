import customtkinter as ctk

def handle_button_press_1(btn_ind_1):  # один хендлер для всех кнопок (вызывается промежуточными хендлерами)
    global lst_btns_1, actual_btn_1, text_entry
    lst_btns_1[actual_btn_1].configure(fg_color='green')
    lst_btns_1[btn_ind_1].configure(fg_color='orange')
    actual_btn_1 = btn_ind_1
    if btn_ind_1 == 9:
        new_text_entry = "0" + text_entry[1:]

    else:
        new_text_entry = str(btn_ind_1 + 1) + text_entry[1:]
    text_entry = new_text_entry
    entry.configure(state="normal")
    entry.delete(0, "end")
    entry.insert(0, text_entry)
    entry.configure(state="readonly")

def handle_button_press_2(btn_ind_2):  # один хендлер для всех кнопок (вызывается промежуточными хендлерами)
    global lst_btns_2, actual_btn_2, text_entry
    lst_btns_2[actual_btn_2].configure(fg_color='green')
    lst_btns_2[btn_ind_2].configure(fg_color='orange')
    actual_btn_2 = btn_ind_2
    if btn_ind_2 == 9:
        new_text_entry = text_entry[:1] + "0" + text_entry[2:]

    else:
        new_text_entry = text_entry[:1] + str(btn_ind_2 + 1) + text_entry[2:]
    text_entry = new_text_entry
    entry.configure(state="normal")
    entry.delete(0, "end")
    entry.insert(0, text_entry)
    entry.configure(state="readonly")

def handle_button_press_3(btn_ind_3):  # один хендлер для всех кнопок (вызывается промежуточными хендлерами)
    global lst_btns_3, actual_btn_3, text_entry
    lst_btns_3[actual_btn_3].configure(fg_color='green')
    lst_btns_3[btn_ind_3].configure(fg_color='orange')
    actual_btn_3 = btn_ind_3
    if btn_ind_3 == 9:
        new_text_entry = text_entry[:2] + "0"

    else:
        new_text_entry = text_entry[:2] + str(btn_ind_3 + 1)
    text_entry = new_text_entry
    entry.configure(state="normal")
    entry.delete(0, "end")
    entry.insert(0, text_entry)
    entry.configure(state="readonly")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title("Задание №6")
root.geometry("500x500")
my_font = ctk.CTkFont(family="Roboto", size=20)

label = ctk.CTkLabel(master=root)
label.configure(
    text="Выберите код:",
    font=my_font,
    text_color="white"
)

text_entry = "111"
entry = ctk.CTkEntry(master=root)
entry.configure(
    justify="center",
    font=my_font,
    width=150,
    height=50
)
entry.insert(0, text_entry)
entry.configure(state="readonly")

scrollable_frame_1 = ctk.CTkScrollableFrame(master=root)
scrollable_frame_1.configure(height=250, width=100)

scrollable_frame_2 = ctk.CTkScrollableFrame(master=root)
scrollable_frame_2.configure(height=250, width=100)

scrollable_frame_3 = ctk.CTkScrollableFrame(master=root)
scrollable_frame_3.configure(height=250, width=100)

rows, columns = 3, 3
for i in range(rows):
    if i == 1:
        root.rowconfigure(index=i, weight=2)
    else:
        root.rowconfigure(index=i, weight=1)

for i in range(columns):
    root.columnconfigure(index=i, weight=1)
scrollable_frame_1.grid(row=1, column=0)
scrollable_frame_2.grid(row=1, column=1)
scrollable_frame_3.grid(row=1, column=2)
label.grid(row=0, column=1)
entry.grid(row=2, column=1)

##### 1 #####

lst_handlers_1 = []
for i in range(10):
    handler_i = lambda i_actual=i: handle_button_press_1(i_actual)
    lst_handlers_1.append(handler_i)

# кнопки внутри scrollable_frame:
lst_btns_1 = []
actual_btn_1 = 0
for i in range(10):
    btn_i = ctk.CTkButton(master=scrollable_frame_1)
    if i == 9:
        btn_i.configure(text=f"0", font=my_font, width=50, height=40, fg_color='green')
    else:
        btn_i.configure(text=f"{i + 1}", font=my_font, width=50, height=40, fg_color='green')
    btn_i.configure(command=lst_handlers_1[i])  # к каждой кнопке привязываем свой промежуточный хендлер
    lst_btns_1.append(btn_i)
lst_btns_1[actual_btn_1].configure(fg_color="orange")

# внутренняя сетка рамки scrollable_frame:
rows, columns = 10, 1
for i in range(rows):
    scrollable_frame_1.rowconfigure(index=i, weight=1)
for i in range(columns):
    scrollable_frame_1.columnconfigure(index=i, weight=1)
for i in range(10):
    btn_i = lst_btns_1[i]
    btn_i.grid(row=i, column=0, padx=20, pady=20)

##### 2 #####

lst_handlers_2 = []
for i in range(10):
    handler_i = lambda i_actual=i: handle_button_press_2(i_actual)
    lst_handlers_2.append(handler_i)

# кнопки внутри scrollable_frame:
lst_btns_2 = []
actual_btn_2 = 0
for i in range(10):
    btn_i = ctk.CTkButton(master=scrollable_frame_2)
    if i == 9:
        btn_i.configure(text=f"0", font=my_font, width=50, height=40, fg_color='green')
    else:
        btn_i.configure(text=f"{i + 1}", font=my_font, width=50, height=40, fg_color='green')
    btn_i.configure(command=lst_handlers_2[i])  # к каждой кнопке привязываем свой промежуточный хендлер
    lst_btns_2.append(btn_i)
lst_btns_2[actual_btn_2].configure(fg_color="orange")

# внутренняя сетка рамки scrollable_frame:
rows, columns = 10, 1
for i in range(rows):
    scrollable_frame_2.rowconfigure(index=i, weight=1)
for i in range(columns):
    scrollable_frame_2.columnconfigure(index=i, weight=1)
for i in range(10):
    btn_i = lst_btns_2[i]
    btn_i.grid(row=i, column=0, padx=20, pady=20)

##### 3 ######

lst_handlers_3 = []
for i in range(10):
    handler_i = lambda i_actual=i: handle_button_press_3(i_actual)
    lst_handlers_3.append(handler_i)

# кнопки внутри scrollable_frame:
lst_btns_3 = []
actual_btn_3 = 0
for i in range(10):
    btn_i = ctk.CTkButton(master=scrollable_frame_3)
    if i == 9:
        btn_i.configure(text=f"0", font=my_font, width=50, height=40, fg_color='green')
    else:
        btn_i.configure(text=f"{i + 1}", font=my_font, width=50, height=40, fg_color='green')
    btn_i.configure(command=lst_handlers_3[i])  # к каждой кнопке привязываем свой промежуточный хендлер
    lst_btns_3.append(btn_i)
lst_btns_3[actual_btn_3].configure(fg_color="orange")

# внутренняя сетка рамки scrollable_frame:
rows, columns = 10, 1
for i in range(rows):
    scrollable_frame_3.rowconfigure(index=i, weight=1)
for i in range(columns):
    scrollable_frame_3.columnconfigure(index=i, weight=1)
for i in range(10):
    btn_i = lst_btns_3[i]
    btn_i.grid(row=i, column=0, padx=20, pady=20)

root.mainloop()
