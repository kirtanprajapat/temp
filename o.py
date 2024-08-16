import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Entry widget to display the calculations
entry = tk.Entry(root, width=16, font=('Arial', 24), bd=8, insertwidth=4, bg='powder blue', justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Function to update the entry widget when a button is pressed
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

# Function to clear the entry widget
def button_clear():
    entry.delete(0, tk.END)

# Function to calculate the expression
def button_equal():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Define buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

for (text, row, col) in buttons:
    if text == '=':
        tk.Button(root, text=text, padx=20, pady=20, bd=8, font=('Arial', 18),
                  command=button_equal).grid(row=row, column=col, sticky="nsew")
    else:
        tk.Button(root, text=text, padx=20, pady=20, bd=8, font=('Arial', 18),
                  command=lambda t=text: button_click(t)).grid(row=row, column=col, sticky="nsew")

# Add a clear button
tk.Button(root, text='C', padx=20, pady=20, bd=8, font=('Arial', 18), command=button_clear).grid(row=4, column=2, sticky="nsew")

# Run the application
root.mainloop()
