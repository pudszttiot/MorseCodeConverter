from tkinter import *

# Create the window
window = Tk()
window.title("Morse Code Converter")
window.geometry('350x350')

# Add a label for the text entry field
lbl = Label(window, text="Enter text to convert:", font=('Arial', 16), fg='black')
lbl.grid(column=0, row=0, columnspan=2, padx=10, pady=10)

# Add an entry field for the user to enter text
txt = Entry(window,width=40)
txt.grid(column=0, row=1, columnspan=2, padx=10)

# Add a label for the output field
lbl2 = Label(window, text="Morse Code:", font=('Arial', 16), fg='blue')
lbl2.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

# Add a text field to display the converted Morse code
output = Text(window, height=10, width=40)
output.grid(column=0, row=3, columnspan=2, padx=10)

# Define the function to convert text to Morse code
def convert_to_morse():
    # Get the text entered by the user
    text = txt.get().upper()

    # Define the Morse code dictionary
    morse_code = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                  'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                  'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                  'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                  '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}

    # Convert the text to Morse code
    morse = ''
    for char in text:
        if char == ' ':
            morse += ' '
        else:
            morse += morse_code[char] + ' '

    # Display the Morse code in the output field
    output.delete('1.0', END)
    output.insert(END, morse)

# Add a button to convert the text to Morse code
btn = Button(window, text="Convert", font=('Arial', 12, 'bold'), bg="#101820", fg="#FEE715", command=convert_to_morse)
btn.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

window.mainloop()
