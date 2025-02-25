from flask import Flask, request, render_template_string

#!/usr/bin/env python3

app = Flask(__name__)
@app.context_processor
def inject_assets():
    modern_css = """
    <style>
      body {
      background: linear-gradient(135deg, #667eea, #764ba2);
      font-family: 'Roboto', sans-serif;
      color: #fff;
      margin: 0;
      padding: 0;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      }
      form {
      background-color: rgba(0, 0, 0, 0.3);
      padding: 30px 40px;
      border-radius: 8px;
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
      display: flex;
      flex-direction: column;
      align-items: stretch;
      width: 100%;
      max-width: 400px;
      }
      input[type="text"], input[type="submit"] {
      padding: 12px;
      border: none;
      border-radius: 4px;
      margin-bottom: 15px;
      font-size: 16px;
      }
      input[type="text"] {
      outline: none;
      }
      input[type="submit"] {
      background-color: #ff4081;
      color: #fff;
      cursor: pointer;
      transition: background-color 0.3s ease;
      }
      input[type="submit"]:hover {
      background-color: #e73370;
      transform: scale(1.05);
      }
      .button-container {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 10px;
        margin-top: 15px;
      }
      .button-container button {
        padding: 15px;
        font-size: 18px;
        border: none;
        border-radius: 4px;
        background-color: #ff4081;
        color: #fff;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.15s ease;
      }
      .button-container button:hover {
        background-color: #e73370;
        transform: scale(0.95);
      }
      }
      h1, h2 {
      text-align: center;
      }
    </style>
    """
    modern_js = """
    <script>
      document.addEventListener("DOMContentLoaded", function(){
        const buttons = document.querySelectorAll('.btn');
        buttons.forEach(btn => {
          btn.addEventListener("click", function(){
            btn.style.transform = "scale(0.95)";
            setTimeout(()=> {
              btn.style.transform = "scale(1)";
            }, 150);
          });
        });
      });
    </script>
    """
    return {"modern_css": modern_css, "modern_js": modern_js}
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>CTF Calculator</title>
    {{ modern_css|safe }}
</head>
<body>
    <h1>CTF Calculator</h1>
    <form method="POST">
        <input type="text" name="expression" placeholder="Enter expression" size="40">
        <input type="submit" value="Calculate">
    </form>
    {% if result is not none %}
    <h2>Result:</h2>
    <p>{{ result }}</p>
    {% endif %}
    {{ modern_js|safe }}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        expression = request.form.get('expression', '')
        try:
            # WARNING: eval is dangerous and this is intentionally vulnerable for a CTF challenge!
            result = eval(expression)
        except Exception as e:
            result = f"Error: {e}"
    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == '__main__':
    # Host on 0.0.0.0 to allow local network access on port 5000
    app.run(host='0.0.0.0', port=5000)
    calc_buttons = '''
    <div class="button-container">
      <button type="button" onclick="appendToExpression('7')">7</button>
      <button type="button" onclick="appendToExpression('8')">8</button>
      <button type="button" onclick="appendToExpression('9')">9</button>
      <button type="button" onclick="appendToExpression('+')">+</button>
      <button type="button" onclick="appendToExpression('4')">4</button>
      <button type="button" onclick="appendToExpression('5')">5</button>
      <button type="button" onclick="appendToExpression('6')">6</button>
      <button type="button" onclick="appendToExpression('-')">−</button>
      <button type="button" onclick="appendToExpression('1')">1</button>
      <button type="button" onclick="appendToExpression('2')">2</button>
      <button type="button" onclick="appendToExpression('3')">3</button>
      <button type="button" onclick="appendToExpression('*')">×</button>
      <button type="button" onclick="appendToExpression('0')">0</button>
      <button type="button" onclick="appendToExpression('.')">.</button>
      <button type="button" onclick="clearExpression()">C</button>
      <button type="button" onclick="appendToExpression('/')">÷</button>
    </div>
    '''

    # Insert the calculator buttons into the form just before its closing tag.
    HTML_TEMPLATE = HTML_TEMPLATE.replace('</form>', calc_buttons + '</form>')

    additional_js = '''
    <script>
      function appendToExpression(value) {
      const exprField = document.querySelector('input[name="expression"]');
      exprField.value += value;
      }
      function clearExpression() {
      const exprField = document.querySelector('input[name="expression"]');
      exprField.value = '';
      }
    </script>
    '''

    # Append our extra JS before the closing of modern_js injection.
    HTML_TEMPLATE = HTML_TEMPLATE.replace('{{ modern_js|safe }}', '{{ modern_js|safe }}' + additional_js)

    # Insert the calculator buttons into the form just before its closing tag.
    HTML_TEMPLATE = HTML_TEMPLATE.replace('</form>', calc_buttons + '</form>')

    additional_js = '''
    <script>
      function appendToExpression(value) {
        const exprField = document.querySelector('input[name="expression"]');
        exprField.value += value;
      }
      function clearExpression() {
        const exprField = document.querySelector('input[name="expression"]');
        exprField.value = '';
      }
    </script>
    '''

    # Append our extra JS before the closing of modern_js injection.
    HTML_TEMPLATE = HTML_TEMPLATE.replace('{{ modern_js|safe }}', '{{ modern_js|safe }}' + additional_js)