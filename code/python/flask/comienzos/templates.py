from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/')
@app.route('/user/<name>')
def user(name=None):
    if name == None:
        users = ['Cesar','Gian','Valeria']
        return render_template('users.html', user=users)
    else:
        return render_template('user.html', user=name)


if __name__ == '__main__':
    app.run(debug=True) #Hacer cambio y que el servidor se reinicie automaticamente 