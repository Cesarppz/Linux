from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola mundo otra vez'

#Parametros de una url 
@app.route('/params/')
@app.route('/params/<name>/')
@app.route('/params/<name>/<int:age>')
def params(name='Default name', age='Default age'):
    return 'Los parametros son:\n.- Name: {name}\n.- Age: {age}'.format(name=name,age=age)


if __name__ == '__main__':
    app.run(debug=True) #Hacer cambio y que el servidor se reinicie automaticamente 