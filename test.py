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

import customtkinter as ctk

# Initialize the main app
ctk.set_appearance_mode("dark")  # Optional: "light" or "dark"
ctk.set_default_color_theme("blue")  # Optional: "blue", "green", "dark-blue"

app = ctk.CTk()  # Main window
app.title("Main Window")
app.geometry("400x300")

def open_new_window():
    # Create a new window (Toplevel)
    new_window = ctk.CTkToplevel(app)
    new_window.title("New Window")
    new_window.geometry("300x200")

    # Add widgets to the new window
    label = ctk.CTkLabel(new_window, text="This is a new window!", font=("Arial", 14))
    label.pack(pady=20)

    close_button = ctk.CTkButton(new_window, text="Close", command=new_window.destroy)
    close_button.pack(pady=10)

# Button to open a new window
open_window_btn = ctk.CTkButton(app, text="Open New Window", command=open_new_window)
open_window_btn.pack(pady=20)

# Run the application
app.mainloop()