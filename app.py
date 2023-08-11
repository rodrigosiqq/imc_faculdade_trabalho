from flask import Flask
from flask import render_template
from flask import request



app = Flask(__name__)


def calcular_imc(peso, altura):
    altura = altura / 100
    imc = peso / (altura ** 2)
    return imc


def avaliar_imc(imc):
    if imc < 18.5:
        return {'imc': imc, 'msg': 'Abaixo do peso'}
    elif imc < 25:
        return {'imc': imc, 'msg': 'Peso normal'}
    elif imc < 30:
        return {'imc': imc, 'msg': 'Acima do peso'}
    else:
        return {'imc': imc, 'msg': 'Obesidade'}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/CalcIMC', methods=['POST'])
def CalcIMC():
    peso = float(request.form.get('peso'))
    altura = float(request.form.get('altura'))
    
    imc = calcular_imc(peso, altura)
    result = avaliar_imc(imc)
    
    return render_template('index.html', result=result)



    

        



if __name__ == "__main__":
    app.run()