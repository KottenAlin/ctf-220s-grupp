import threading
import tkinter as tk
from flask import Flask, request, render_template_string

#!/usr/bin/env python3
"""
This file implements a simple graphical calculator using tkinter and
also hosts a basic web version on the local network using Flask.
Run this file on a host in your local network;
the GUI calculator will open locally, and you can access the web calculator
by browsing to http://<host-ip>:8000.
"""


# ---------------------------
# Flask Web Calculator Setup
# ---------------------------
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def web_calculator():
    result = ""
    expr = ""
    if request.method == "POST":
        expr = request.form.get("expression", "")
        try:
            # Using eval in a controlled namespace
            result = str(eval(expr, {"__builtins__": None}, {}))
        except Exception:
            result = "Error"
    html = """
    <!doctype html>
    <html>
      <head>
        <title>Galculator Web</title>
      </head>
      <body>
        <h1>Galculator Web</h1>
        <form method="post">
          <input type="text" name="expression" value="{{expr}}" size="30">
          <input type="submit" value="Calculate">
        </form>
        <p>Result: {{result}}</p>
      </body>
    </html>
    """
    return render_template_string(html, expr=expr, result=result)

def run_flask():
    # Host on all available interfaces at port 8000

    print("Flask server starting on http://0.0.0.0:8000")
    app.run(host="0.0.0.0", port=8000, debug=False)

# ---------------------------
# Tkinter GUI Calculator Setup
# ---------------------------
def run_tkinter():
    root = tk.Tk()
    root.title("Galculator")

    entry = tk.Entry(root, width=40, borderwidth=5, font=("Arial", 16))
    entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    def button_click(value):
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(0, current + value)

    def button_clear():
        entry.delete(0, tk.END)

    def button_equal():
        try:
            result = eval(entry.get(), {"__builtins__": None}, {})
            entry.delete(0, tk.END)
            entry.insert(0, str(result))
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")

    # Define button labels and grid positions
    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ]

    for (text, row, col) in buttons:
        # Assign the equal button a different command
        if text == "=":
            action = button_equal
        else:
            action = lambda x=text: button_click(x)
        tk.Button(root, text=text, padx=40, pady=20, font=("Arial", 14), command=action)\
            .grid(row=row, column=col)

    # Clear and Quit buttons spanning multiple columns
    tk.Button(root, text="Clear", padx=79, pady=20, font=("Arial", 14), command=button_clear)\
        .grid(row=5, column=0, columnspan=2)
    tk.Button(root, text="Quit", padx=79, pady=20, font=("Arial", 14), command=root.quit)\
        .grid(row=5, column=2, columnspan=2)

    root.mainloop()

# ---------------------------
# Main Execution
# ---------------------------
if __name__ == "__main__":
    # Start the Flask server in a separate thread (daemon thread)
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    print("Starting Flask server...")
    flask_thread.start()

    # Run the Tkinter GUI (this call is blocking)
    print("Starting Tkinter GUI...")
    run_tkinter()