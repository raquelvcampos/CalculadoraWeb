from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('calculator.html')

@app.route('/resultado', methods=['POST'])
def calculate():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operacao = request.form['operacao']

    if operacao == 'add':
        resultado = num1 + num2
    elif operacao == 'subtract':
        resultado = num1 - num2
    elif operacao == 'multiply':
        resultado = num1 * num2
    elif operacao == 'divide':
        if num2 != 0:
            resultado = num1 / num2
        else:
            resultado = "Divisão por zero não é permitida."
    else:
        return "Operação inválida"

    return render_template('resultado.html', resultado=resultado)

    return render_template('calculator.html', resultado=resultado)


if __name__ == '__main__':
    app.run(debug=True)