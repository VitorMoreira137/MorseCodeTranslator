# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
#
# x = thisdict.keys()
#
# print(x)
# print(type(x))
#
# a = thisdict["brand"]
# print(a)

# import customtkinter as ctk
#
# # Initialize the main app
# ctk.set_appearance_mode("dark")  # Optional: "light" or "dark"
# ctk.set_default_color_theme("blue")  # Optional: "blue", "green", "dark-blue"
#
# app = ctk.CTk()  # Main window
# app.title("Main Window")
# app.geometry("400x300")
#
# def open_new_window():
#     # Create a new window (Toplevel)
#     new_window = ctk.CTkToplevel(app)
#     new_window.title("New Window")
#     new_window.geometry("300x200")
#
#     # Add widgets to the new window
#     label = ctk.CTkLabel(new_window, text="This is a new window!", font=("Arial", 14))
#     label.pack(pady=20)
#
#     close_button = ctk.CTkButton(new_window, text="Close", command=new_window.destroy)
#     close_button.pack(pady=10)
#
# # Button to open a new window
# open_window_btn = ctk.CTkButton(app, text="Open New Window", command=open_new_window)
# open_window_btn.pack(pady=20)
#
# # Run the application
# app.mainloop()

from morse_code_dictionary import morse_code_dict, morse_to_ASCII_dict

# def morse2ASII_translator():



# # plain_text = "Bom dia"  # Desired Output = "-... --- -- / -.. .. .-"
# morse_code = "-... --- -- / -.. .. .-"  # Desired Output = "Bom dia"
# morse_array = morse_code.split(" ") # Each morse code element is composed by a set of dots an dashes
# #['-...', '---', '--', '/', '-..', '..', '.-']
# # print(morse_array)
# ASCII_array = []
#
#
# keys_array = list(morse_to_ASCII_dict.keys())
# # print(keys_array)
#
# for k in range(len(morse_array)):
#     element = morse_array[k]
#     # print(element)
#     for l in range(len(morse_to_ASCII_dict)):
#         if element == keys_array[l]:
#             ASCII_array.append(morse_to_ASCII_dict.get(element))
# print(ASCII_array)
#
# def morse2ASII_translator(text):
#     # morse_code = "-... --- -- / -.. .. .-"  # Desired Output = "Bom dia"
#     morse_code = text
#     morse_array = morse_code.split(" ")  # Each morse code element is composed by a set of dots an dashes
#     ASCII_array = []
#     keysArray = list(morse_to_ASCII_dict.keys())
#
#     for k in range(len(morse_array)):
#         element = morse_array[k]
#         for l in range(len(morse_to_ASCII_dict)):
#             if element == keysArray[l]:
#                 ASCII_array.append(morse_to_ASCII_dict.get(element))
#     ASCII_Text = "".join(ASCII_array) # Turns the list format into a stringlike format
#     return ASCII_Text
#
# answer = morse2ASII_translator("-... --- -- / -.. .. .-")
# print(answer + " OK")



import customtkinter as ctk

def switch_event():
    print("switch toggled, current value:", switch_var.get())

# Initialize the main app
ctk.set_appearance_mode("dark")  # Optional: "light" or "dark"
ctk.set_default_color_theme("blue")  # Optional: "blue", "green", "dark-blue"

app = ctk.CTk()  # Main window
app.title("Main Window")
app.geometry("400x300")

switch_var = ctk.StringVar(value="on")
switch = ctk.CTkSwitch(app, text="CTkSwitch", command=switch_event,
                                 variable=switch_var, onvalue="on", offvalue="off")
switch.grid(row=2, column=1)

app.mainloop()