import tkinter as tk

class SimpleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple GUI App")
        
        # Create and pack a label
        self.label = tk.Label(root, text="Hello, World!")
        self.label.pack(pady=20)
        
        # Create and pack a button
        self.button = tk.Button(root, text="Click Me!", command=self.button_click)
        self.button.pack(pady=10)
        
    def button_click(self):
        self.label.config(text="Button was clicked!")

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleApp(root)
    root.mainloop()