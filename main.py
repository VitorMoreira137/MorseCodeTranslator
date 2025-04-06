from morse_code_dictionary import morse_code_dict, morse_to_ASCII_dict
import customtkinter as ctk
import Concepts
from morse_led_sound import play_morse_with_led


def translator():
    """ Translates plain text (ASCII) to morse code"""
    plain_text = var1.get() # Stores what user types in the Entry1
    morse_array = []
    keys_array = list(morse_code_dict.keys())

    for i in range(len(plain_text)): # Iterate through each plain text "letter"
        char = plain_text[i]
        for j in range(len(morse_code_dict)): # Iterate through each element in the morse_code_dictionary
            if char == keys_array[j]:
                morse_array.append(morse_code_dict.get(char)) # The get() method returns the value of the item with the specified key.

    label3.configure(text=morse_array)

    sound_btn.configure(state="normal") #Make the sound button clickable, only when morse code exists in label 3

    return morse_array

def morse2ASII_translator():
    """ translate morse code to plain text (ASCII) """
    morse_code = var1.get() # Stores what user types in the Entry1
    morse_code = morse_code.upper() # Since a dictionary can't have duplicate keys (i.e., you can't map the same Morse code to both 'A' and 'a' in separate entries)
    morse_array = morse_code.split(" ")  # Each morse code element is composed by a set of dots and dashes, separeted by whites[ace
    ASCII_array = []
    keysArray = list(morse_to_ASCII_dict.keys())

    for k in range(len(morse_array)):
        element = morse_array[k]
        for l in range(len(morse_to_ASCII_dict)):
            if element == keysArray[l]:
                ASCII_array.append(morse_to_ASCII_dict.get(element))
    ASCII_Text = "".join(ASCII_array) # Turns the list format into a stringlike format

    label3.configure(text=ASCII_Text)

    sound_btn.configure(state="normal") #Makes the sound button available to click

    return ASCII_Text

def switch_translation():
    """Function that changes the function linked to the "Translate" button.
    Plain text ➔ Morse Code
    Morse Code ➔ Plain text """

    var1.set("")  # clears the input field
    label3.configure(text="")  #clears the output as well
    sound_btn.configure(state="disabled")

    if switch_var.get() == "on":
        label1_content = "Type your text message here:"
        label2_content = "⏬ Morse code will be translated here ⏬"
        translate_btn.configure(command=translator) # changes the function executed when translate button is pressed
    elif switch_var.get() == "off":
        label1_content = "Type your morse code here:"
        label2_content = "⏬ ASCII text will be translated here ⏬"
        translate_btn.configure(command=morse2ASII_translator) # changes the function executed when translate button is pressed

    label1.configure(text=label1_content)
    label2.configure(text=label2_content)

def open_help_window():
    """ Opens a help window with concepts"""
    # Create a new window (Toplevel)
    help_window = ctk.CTkToplevel(app)
    help_window.title("Help")
    help_window.geometry("500x600")

    # Create a scrollable textbox
    textbox = ctk.CTkTextbox(help_window, wrap="word", width=480, height=350, font=("Arial", 14),text_color="#19adfc")
    textbox.pack(pady=10, padx=10, fill="both", expand=True)

    # Insert text from concepts.py
    textbox.insert(index="1.0", text=Concepts.morse_code_text)

    close_btn = ctk.CTkButton(help_window, text="Close", command=help_window.destroy, fg_color="red", width=15)
    close_btn.pack(pady=10)

##  >>> GUI Window Creation --------------------------------------------------------------------------------------------
app = ctk.CTk()
app.title("Morse Code Translator")
app.geometry("1200x600")
app.grid_columnconfigure(index=0, weight=1)

##  >>> Variables ------------------------------------------------------------------------------------------------------
var1 = ctk.StringVar() # Stores what the user types
switch_var = ctk.StringVar(value="on") # Stores the value of the switch button

## >>> GUI Elements ----------------------------------------------------------------------------------------------------

# Title
label0 = ctk.CTkLabel(app, text=" >>> Morse Code Translator <<<",font=("Arial Black", 40),text_color="#19adfc")

# Instruction label
label1 = ctk.CTkLabel(app, text="Type your message (ASCII Text) here:",font=("Arial", 28),text_color="#19adfc")

# Input box
txt_box1 = ctk.CTkEntry(app, font=("Arial", 20), textvariable=var1, width=1000, height= 100, fg_color="white",
                        text_color="blue")

#Translate button
translate_btn = ctk.CTkButton(app, text = "Translate", font=("Arial", 14), command=translator, width=100, height=50)

# Help Button
help_btn = ctk.CTkButton(app, text = "❔", command=open_help_window, width=10)

#Toggle translation button
toggle_btn = ctk.CTkSwitch(app, text="Toogle Translation", command=switch_translation, variable= switch_var,
                           onvalue="on", offvalue="off")

#LED (colored label) that blinks n sync with the sound
# ➔ led_widget is a keyword argument passed to the function play_morse_with_led()
# ➔ led_widget receives the value led_label, which is your CustomTkinter label simulating a LED.
# ➔ Inside play_morse_with_led(), it checks if led_widget exists (if led_widget:) and then changes its color as part of
# the "blinking" effect.
# ➔ Using led_widget as an optional parameter makes the function flexible. For example:
# You can call play_morse_with_led(morse_code) with no LED for just the sound.
# Or pass led_widget=some_widget to make something flash in sync.

led_label = ctk.CTkLabel(app, text="", width=50, height=50, corner_radius=25, fg_color="black")

#Play sound button
#.cget("text") is a Tkinter method that retrieves the current value of a widget property.
#In this case, it's getting the text from label3
# A lambda is an anonymous (unnamed) function in Python. It allows you to define a small function in a single line,
# without needing to use def.
# it’s used to call a function with arguments, which isn’t directly possible when assigning to command="something" in Tkinter.

sound_btn = ctk.CTkButton(app, font=("Arial", 14),
                          command=lambda: play_morse_with_led(label3.cget("text"),led_widget=led_label),
                          width=120, height=50, state="disabled", text="🔊 Play Sound")

# Label that shows if the text below is morse or plain text
label2 = ctk.CTkLabel(app, text="⏬ Morse code will be translated here ⏬", font=("Arial", 28),
                      fg_color="transparent",text_color="#19adfc", width=1000, height=80)
# Output
label3 = ctk.CTkLabel(app, text="",font=("Arial", 28), fg_color="#4a4a48",text_color="#19adfc",
                      width=1000, height=100, corner_radius=15)

# >>> GUI Element Placement -------------------------------------------------------------------------------------------

label0.place(relx=0.5, y=30, anchor="center")        # Title
label1.place(relx=0.5, y=80, anchor="center")        # Instruction label
txt_box1.place(relx=0.5, y=160, anchor="center")     # Input box

translate_btn.place(relx=0.2, y=250, anchor="center") #Translate button
toggle_btn.place(relx=0.4, y=250, anchor="center") #Toggle translation button
sound_btn.place(relx=0.6, y=250, anchor="center") #play sound button
led_label.place(relx=0.75, y=250, anchor="center") #LED that blinks when sound is played

label2.place(relx=0.5, y=325, anchor="center")       # "Translated here"
label3.place(relx=0.5, y=420, anchor="center")       # Output

help_btn.place(relx=1.0, y=10, anchor="ne", x=-20)   # Help Button Top right

#The mainloop() method puts everything on the display, and responds to user input until the program terminates.
app.mainloop()


