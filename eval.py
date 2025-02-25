import tkinter as tk
from tkinter import ttk
import webbrowser
import threading
import time

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CTF Calculator")
        self.root.configure(bg='#2b2b2b')
        
        # Entry field for expression
        self.expression = tk.StringVar()
        self.entry = ttk.Entry(root, textvariable=self.expression, font=('Courier', 14))
        self.entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky='nsew')
        
        # Button layout
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        
        # Create and place buttons
        row = 1
        col = 0
        for button in buttons:
            cmd = lambda x=button: self.click(x)
            btn = tk.Button(root, text=button, command=cmd, width=5, height=2,
                          bg='#404040', fg='white', font=('Courier', 12))
            btn.grid(row=row, column=col, padx=2, pady=2)
            col += 1
            if col > 3:
                col = 0
                row += 1
                
        # Clear button
        clear_btn = tk.Button(root, text='C', command=self.clear, width=5, height=2,
                             bg='#ff4444', fg='white', font=('Courier', 12))
        clear_btn.grid(row=row, column=0, columnspan=2, padx=2, pady=2)
        
    def click(self, char):
        if char == '=':
            try:
                result = eval(self.expression.get())
                self.expression.set(result)
            except:
                self.expression.set('Error')
        else:
            current = self.expression.get()
            self.expression.set(current + char)
            
    def clear(self):
        self.expression.set('')
        
        
def rickroll():
    time.sleep(300)  # Wait 5 minutes
    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

if __name__ == '__main__':


    # Start rickroll timer when app launches
    threading.Thread(target=rickroll, daemon=True).start()
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()