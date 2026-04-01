import customtkinter as ctk

def handle_switch_choice():
    global var_switch
    if var_switch.get():
        ctk.set_appearance_mode("light")
    else:
        ctk.set_appearance_mode("dark")

def handle_slider_1_choice(value):
    if var_slider_1.get() < 50.0:
        slider_1.configure(button_color="red", button_hover_color="red")
        label_1.configure(text="красный ползунок")
    if var_slider_1.get() == 50.0:
        slider_1.configure(button_color="green", button_hover_color="green")
        label_1.configure(text="зелёный ползунок")
    if var_slider_1.get() > 50.0:
        slider_1.configure(button_color="blue", button_hover_color="blue")
        label_1.configure(text="синий ползунок")


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title("Задание №4")
root.geometry("500x550")
my_font = ctk.CTkFont(family="Roboto", size=20)

var_switch = ctk.BooleanVar()
switch = ctk.CTkSwitch(master=root, variable=var_switch, onvalue=True, offvalue=False)
switch.configure(text="Тёмная тема", font=my_font)
switch.configure(command=handle_switch_choice)
var_switch.set(False)

# Slider - ползунок:
var_slider_1 = ctk.DoubleVar()
slider_1 = ctk.CTkSlider(
    master=root,
    from_=0, to=100,
    variable=var_slider_1,
    orientation="horizontal",
    button_color="red",
    button_hover_color="red"
)
slider_1.configure(command=handle_slider_1_choice)
slider_1.set(0)  # значение на старте
label_1 = ctk.CTkLabel(master=root, text="красный ползунок", font=my_font)  # label будет отображать значение ползунка


# взаимодействие со Slider:
var_slider_1.get()
# больше о Slider - в документации:
# https://customtkinter.tomschimansky.com/documentation/widgets/slider

switch.pack(pady=(100, 10))
slider_1.pack(pady=(200, 10))  # отступ 100px сверху и 10px снизу
label_1.pack(pady=(10, 100))

root.mainloop()
