from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = 'Cesar'
    return render_template('index_ext.html',name=name)


@app.route('/user/')
def user():
    names = ['Cesar','Valeria','Andres'] 
    return render_template('users_ext.html', users=names)


if __name__ == '__main__':
    app.run(debug=True) #Hacer cambio y que el servidor se reinicie automaticamente 