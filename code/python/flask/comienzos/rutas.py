from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola mundo otra vez'

#Parametros de una url 
@app.route('/params')
def params():
    p1 = request.args.get('p1','No se encuentra P1')
    p2 = request.args.get('p2','No se encuentra P2')
    return 'Los parametros son: {}, {}'.format(p1, p2)


if __name__ == '__main__':
    app.run(debug=True) #Hacer cambio y que el servidor se reinicie automaticamente 