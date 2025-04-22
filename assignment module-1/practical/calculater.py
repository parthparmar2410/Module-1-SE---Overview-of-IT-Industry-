import tkinter as tk

# Function to evaluate the expression
def evaluate_expression(expression):
    try:
        result = str(eval(expression))  # Evaluate the expression
        entry_var.set(result)
    except Exception as e:
        entry_var.set("Error")

# Function to update the expression in the text box
def update_expression(symbol):
    current_expression = entry_var.get()
    new_expression = current_expression + str(symbol)
    entry_var.set(new_expression)

# Function to clear the expression
def clear_expression():
    entry_var.set("")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create a variable to hold the current expression
entry_var = tk.StringVar()

# Create the input field (entry)
entry = tk.Entry(root, textvariable=entry_var, font=('Arial', 24), borderwidth=2, relief='solid', width=14, justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Define the buttons and their corresponding functions
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)
]

# Create buttons and add them to the grid
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, font=('Arial', 18), command=lambda: evaluate_expression(entry_var.get()))
    elif text == 'C':
        button = tk.Button(root, text=text, font=('Arial', 18), command=clear_expression)
    else:
        button = tk.Button(root, text=text, font=('Arial', 18), command=lambda symbol=text: update_expression(symbol))
    
    button.grid(row=row, column=col, sticky="nsew", ipadx=10, ipady=10)

# Make the buttons expand to fill the grid
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

# Run the application
root.mainloop()
