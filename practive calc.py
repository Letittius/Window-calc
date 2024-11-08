import tkinter as tk

#adding gui interface

#finction to make calculations
root = tk.Tk()
root.title("Window Calculator") #title of window
root.geometry("500x400") #sets window size
#locks window size
root.resizable(width=False, height=False)

#defining font and titles along with other parts of interface
#name of font, then size, then style if needed
title_font = ("Georgia", 16, "bold")
label_font = ("Georgia", 12)
entry_font = ("Georgia", 12)
button_font = ("Georgia", 12, "bold")

#title Label with font
title_label = tk.Label(root, text="Window Calculator", font=title_font)
title_label.pack(pady=20)
#pad is the code, y and or x go after for the direction. x is horizontal padding and y is vertical padding

#frame to group entry fields
frame_entries = tk.Frame(root)
frame_entries.pack(pady=10)

#label and entry for the first number
label_num1 = tk.Label(frame_entries, text="Enter the first number:", font=label_font)
label_num1.grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_num1 = tk.Entry(frame_entries, width=20, font=entry_font)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

# Label and entry for the second number
label_num2 = tk.Label(frame_entries, text="Enter the second number:", font=label_font)
label_num2.grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_num2 = tk.Entry(frame_entries, width=20, font=entry_font)
entry_num2.grid(row=1, column=1, padx=10, pady=10)

# Function to perform calculations
def calculate():
    try:
        number1 = float(entry_num1.get())
        number2 = float(entry_num2.get())
        
        # Perform calculations
        result_add = number1 + number2
        result_sub = number1 - number2
        result_mul = number1 * number2
        result_div = number1 / number2 if number2 != 0 else "Cannot divide by zero"
        
        # Update result label with each operation result
        result_label.config(text=f"Add: {result_add} | Sub: {result_sub} | Mul: {result_mul} | Div: {result_div}")

    except ValueError:
        result_label.config(text="Please enter valid numbers.")

# Calculate button with Georgia font
calculate_button = tk.Button(root, text="Calculate", command=calculate, font=button_font, bg="#4CAF50", fg="white")
calculate_button.pack(pady=20)

# Label to display results with Georgia font
result_label = tk.Label(root, text="Results will appear here", font=label_font)
result_label.pack(pady=20)

#runs main loop- must be at the bottom
root.mainloop()
    