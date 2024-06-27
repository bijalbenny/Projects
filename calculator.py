import tkinter as tk

# Function to update the expression in the Entry widget
def update_expression(key):
    current_text = entry.get()
    new_text = current_text + key
    entry.delete(0, tk.END)
    entry.insert(0, new_text)

# Function to calculate the result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create the Entry widget to display expression and results
entry = tk.Entry(root, width=20, font=('Arial', 18), justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define the buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Create and place the buttons in the grid
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18),
                       command=lambda key=text: update_expression(key))
    button.grid(row=row, column=col, padx=5, pady=5)

# Special handling for '=' button (calculate result)
equal_button = tk.Button(root, text='=', width=5, height=2, font=('Arial', 18),
                         command=calculate)
equal_button.grid(row=4, column=2, padx=5, pady=5)

# Run the main loop
root.mainloop()
