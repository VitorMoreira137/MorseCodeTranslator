from morse_code_dictionary import morse_code_dict
import customtkinter as ctk
import Concepts
from PIL import Image

def translator():
    # Outputs
    plain_text = var1.get()
    # plain_text = "Bom dia"  # Desired Output = "-... --- -- / -.. .. .-"
    morse_array = []
    keys_array = list(morse_code_dict.keys())

    for i in range(len(plain_text)):
        char = plain_text[i]
        for j in range(len(morse_code_dict)):
            if char == keys_array[j]:
                morse_array.append(morse_code_dict.get(char))

    print(morse_array)
    label2.configure(text=morse_array)

def open_help_window():
    # Create a new window (Toplevel)
    help_window = ctk.CTkToplevel(app)
    help_window.title("Help")
    help_window.geometry("300x200")

    # Create a scrollable textbox
    textbox = ctk.CTkTextbox(help_window, wrap="word", width=480, height=350, font=("Arial", 12))
    textbox.pack(pady=10, padx=10, fill="both", expand=True)

    # Insert text from concepts.py
    textbox.insert(index="1.0", text=Concepts.morse_code_text)

    close_btn = ctk.CTkButton(help_window, text="Close", command=help_window.destroy)
    close_btn.pack(pady=10)


app = ctk.CTk()
app.title("Morse Code Translator")
app.geometry("1200x400")
app.grid_columnconfigure(index=0, weight=1)

var1 = ctk.StringVar() # Stores what the user types

label1 = ctk.CTkLabel(app, text="ASCII Text:",font=("Arial", 28)).grid(row=0, column=0, padx=20, pady=20)
txt_box1 = ctk.CTkEntry(app, placeholder_text="Place your text here", textvariable=var1, width=500, height= 70,
                        fg_color="white", text_color="blue")
txt_box1.grid(row=1, column=0, padx=20, pady=20,sticky="ew")

btn = ctk.CTkButton(app, text = "Translate", font=("Arial", 14), command=translator, width=100, height=50)
btn.grid(row=2, column=0, padx=20, pady=20)

help_btn = ctk.CTkButton(app, text = "?", command=open_help_window, width=10)
help_btn.grid(row=0, column=2, padx=20, pady=20)

label2 = ctk.CTkLabel(app, text="Morse Code will be translated here", font=("Arial", 28),
                      fg_color="transparent",text_color="#19adfc", width=1000, height=100)
label2.grid(row=3, column=0, padx=20, pady=20)

app.mainloop()


