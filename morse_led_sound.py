import time # Used to control the timing between Morse code symbols
import winsound # Used to play sound on Windows

# Constants for Morse timing (in milliseconds)
DOT_DURATION = 100 # Duration of a dot
DASH_DURATION = DOT_DURATION * 3 # A dash is 3x longer than a do
FREQUENCY = 750 # Frequency of the beep sound in Hz
SYMBOL_PAUSE = DOT_DURATION # Pause between symbols (dot or dash)
LETTER_PAUSE = DOT_DURATION * 3 # Pause between letters
WORD_PAUSE = DOT_DURATION * 7 # Pause between words

def play_morse_with_led(morse_code_list, led_widget=None):
    """Plays Morse code as sound and flashes a 'LED' widget (if provided).

        Parameters:
            morse_code_list (list of str): Morse code symbols to play (e.g., ['.-', '-...', '/']).
            led_widget (optional): A CustomTkinter Label to act as the blinking LED.
        """
    def led_on(): # Turns the LED "on" by changing its color to yellow
        if led_widget : #if led_widget is not None: (in this case it exists because it was passed as a parameter to the fuction)
            led_widget.configure(fg_color="yellow")
            led_widget.update()

    def led_off(): #Turns the LED "off" by changing its color to black
        if led_widget: #if led_widget is not None:
            led_widget.configure(fg_color="black")
            led_widget.update()

    # Iterate through each Morse code "word" or "letter" in the list
    for symbol in morse_code_list:
        if symbol == '/':
            time.sleep(WORD_PAUSE / 1000) # Represents a space between words
        elif symbol == ' ':
            time.sleep(LETTER_PAUSE / 1000)
        else:
            for char in symbol:  # For each character (dot or dash) in the Morse symbol
                if char == '.':
                    led_on()
                    winsound.Beep(FREQUENCY, DOT_DURATION)
                    led_off()
                elif char == '-':
                    led_on()
                    winsound.Beep(FREQUENCY, DASH_DURATION)
                    led_off()
                time.sleep(SYMBOL_PAUSE / 1000)  # Short pause between each dot or dash in the same letter

            time.sleep(LETTER_PAUSE / 1000) # Extra pause after each full letter
