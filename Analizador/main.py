from flask import Flask, render_template, request
from lexer import Lexer
from parser import Parser

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        curp = request.form['curp']
        lexer = Lexer()
        parser = Parser(lexer)
        
        try:
            resultado = parser.parse(curp)
            print("Tokens extraídos:", resultado)  
        except ValueError as e:
            resultado = {'error': str(e)}
            print("Error:", str(e))  

    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
