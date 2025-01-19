import tkinter as tk
from tkinter import font

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.resizable(False,False)

def center():
    width, height = 320, 350  # Desired width and height of the GUI window
    screen_width = root.winfo_screenwidth()  # Get the width of the screen
    screen_height = root.winfo_screenheight()  # Get the height of the screen
    x = int(screen_width / 2 - width / 2)  # Calculate x-coordinate for centering
    y = int(screen_height / 2 - height / 2)  # Calculate y-coordinate for centering
    root.geometry(f"{width}x{height}+{x}+{y}") 

center();

# Define a custom font
button_font = font.Font(size=14, weight="bold")

# Display area
display = tk.Entry(root, font=("Arial", 25), justify="right", bd=10, insertwidth=2, width=17, borderwidth=2)
display.grid(row=0, column=0, columnspan=4, pady=4,padx=4)
display.insert(0, "0")

# Command Function make
def add_to_display(value):
    print(value);
def clear_display():
    print("clear value");
def delete_last():
    print("delete last value");
def calculate_result():
    print("calculate_result");
    
# Button layout
buttons = [
    ("(", lambda: add_to_display("(")), (")", lambda: add_to_display(")")),
    ("C", clear_display), ("<", delete_last),
    ("7", lambda: add_to_display("7")), ("8", lambda: add_to_display("8")),
    ("9", lambda: add_to_display("9")), ("/", lambda: add_to_display("/")),
    ("4", lambda: add_to_display("4")), ("5", lambda: add_to_display("5")),
    ("6", lambda: add_to_display("6")), ("x", lambda: add_to_display("*")),
    ("1", lambda: add_to_display("1")), ("2", lambda: add_to_display("2")),
    ("3", lambda: add_to_display("3")), ("-", lambda: add_to_display("-")),
    (".", lambda: add_to_display(".")), ("0", lambda: add_to_display("0")),
    ("00", lambda: add_to_display("00")), ("+", lambda: add_to_display("+")),
    ("=", calculate_result)
]

# Button colors
operator_color = "#FFFFFF"
number_color = "#FFFFFF"
background_color = "#EBEBEB"

# Create buttons and place them in the grid
row = 1
col = 0
for button,button_command  in buttons:
    if button in ["(", ")","C", "<"]:
        btn = tk.Button(
            root,
            text=button,
            font=button_font,
            bg=operator_color,
            fg="blue",
            height=1,
            width=5,
            command=button_command
        )
    elif button in ["="]:
        btn = tk.Button(
            root,
            text=button,
            font=button_font,
            bg=operator_color,
            fg="green",
            height=1,
            width=25,
            command=button_command
        )
    elif button in ["+", "-", "x", "/"]:
        btn = tk.Button(
            root,
            text=button,
            font=button_font,
            bg=operator_color,
            fg="red",
            height=1,
            width=5,
            command=button_command
        )
    else:
        btn = tk.Button(
            root,
            text=button,
            font=button_font,
            bg=number_color,
            fg="black",
            height=1,
            width=5,
            command=button_command
        )
    if button in ["="]:
        btn.grid(row=6, column=0, columnspan=4, padx=5, pady=5)
    else:
        btn.grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col > 3:
        col = 0
        row += 1

# Run the main loop
root.mainloop()
