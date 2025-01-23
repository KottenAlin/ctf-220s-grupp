import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Dangerous Calculator")
        
        # Entry field
        self.display = tk.Entry(self.window, width=35, justify='right')
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Buttons layout
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        self.style = ttk.Style()
        self.style.configure('Modern.TButton', padding=5, font=('Helvetica', 10))

        buttons = [
            {'text': '7', 'bg': '#f0f0f0'}, {'text': '8', 'bg': '#f0f0f0'}, 
            {'text': '9', 'bg': '#f0f0f0'}, {'text': '/', 'bg': '#e1e1e1'},
            {'text': '4', 'bg': '#f0f0f0'}, {'text': '5', 'bg': '#f0f0f0'}, 
            {'text': '6', 'bg': '#f0f0f0'}, {'text': '*', 'bg': '#e1e1e1'},
            {'text': '1', 'bg': '#f0f0f0'}, {'text': '2', 'bg': '#f0f0f0'}, 
            {'text': '3', 'bg': '#f0f0f0'}, {'text': '-', 'bg': '#e1e1e1'},
            {'text': '0', 'bg': '#f0f0f0'}, {'text': '.', 'bg': '#f0f0f0'}, 
            {'text': '=', 'bg': '#4CAF50'}, {'text': '+', 'bg': '#e1e1e1'}
        ]

        row = 1
        col = 0
        for button in buttons:
            cmd = lambda x=button: self.click(x)
            tk.Button(self.window, text=button, width=7, command=cmd).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def click(self, key):
        if key == '=':
            try:
                # WARNING: eval() is dangerous as it can execute arbitrary code
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                messagebox.showerror("Error", "Invalid input!")
                self.display.delete(0, tk.END)
        else:
            self.display.insert(tk.END, key)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()