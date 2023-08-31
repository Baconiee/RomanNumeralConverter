from tkinter import *


def convert_to_integer(roman_numeral):
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0

    for symbol in reversed(roman_numeral):
        value = roman_numerals[symbol]

        if value < prev_value:
            total -= value
        else:
            total += value

        prev_value = value

    return total


def RomanNumerals():
    roman_numeral = entry_area.get().upper()

    if not all(symbol in ['I', 'V', 'X', 'L', 'C', 'D', 'M'] for symbol in roman_numeral):
        result_label.config(text="Invalid Roman Numeral", font=("Verdena", 10, "bold"))
    else:
        integer_value = convert_to_integer(roman_numeral)
        if integer_value > 4999:
            result_label.config(text="Enter a valid Roman Numeral up to 4999", font=("Verdena", 10, "bold"))
        else:
            result_label.config(text=f"Your Integer Value Is: {integer_value}", font=("Verdena", 10, "bold"))

    result_label.place(y=180, x=60)


# User Interface
root = Tk()
root.title("Converter")
root.geometry("350x230")
up_title_label = Label(root, text="Roman Numeral Converter", font=("Verdena", 17, "bold"))
up_title_label.config(bg="#CD3333")
up_title_label.pack()
explain_label = Label(root, text="Write the Roman Numeral", font=("Verdena", 17, "normal"))
explain_label.config(pady=10)
explain_label.pack()
entry_area = Entry(root)
entry_area.pack()
clear_button = Button(root, text="Clear", command="")
clear_button.place(x=10, y=110)
clear_button.config(width=10, height=2)
calculate_button = Button(root, text="Convert", command=RomanNumerals)
calculate_button.place(x=260, y=110)
calculate_button.config(width=10, height=2)
result_label = Label()
result_label.place(y=180, x=60)

root.mainloop()
