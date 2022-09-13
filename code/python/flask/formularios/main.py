import json

from flask import Flask
from flask import render_template
from flask import request
#Cookie
from flask import make_response 
# Session
from flask import session
#Tablas
from tables import CommentForm, LoginForm, SignupForm
# Seguridad
from flask_wtf.csrf import CSRFProtect 
# Redireccionar 
from flask import url_for
from flask import redirect
#Message 
from flask import flash

from config import DeveloperConfig
from models import db, User, Comment

from helpers import date_format

#Email
from flask_mail import Mail, Message

#Threading
import threading
from flask import copy_current_request_context


app = Flask(__name__)
app.config.from_object(DeveloperConfig)
csrf = CSRFProtect()
mail = Mail()


def send_email(user_email, user):
    msg = Message(  'Gracias por su registro!', 
                        sender=app.config['MAIL_USERNAME'],
                        recipients = [user_email]
                    )

    msg.html = render_template('email.html', user=user)
    mail.send(msg)


@app.before_request
def before_request():
    if 'username' not in session and request.endpoint  in ['cookie','index','comment']:
        return redirect(url_for('signup'))

    elif 'username' in session and request.endpoint in ['login', 'signup']:
        return redirect(url_for('index'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/review/', methods=['GET'])
@app.route('/review/<int:page>', methods=['GET'])
def review(page=1):
    raw_number = Comment.query.count()
    raw_number = int(raw_number)
    limit_page = raw_number / 3 
    if raw_number%limit_page !=0:
        limit_page = int(limit_page) + 1

    comment_list = Comment.query.join(User).add_columns(
                                                User.name, 
                                                Comment.comment,
                                                Comment.created_at
                                                       ).paginate(page,3,False) #El primero atributo es en la pag en la que va a comenzar, el segundo es el size del bloque por pag, el ultimo es bool que si es verdadero y no hay info en ese bloque me lleva a un error 404

    
    return render_template('review.html', comments=comment_list, page=page, limit_page=limit_page, date_format=date_format)


@app.route('/signup', methods=['GET','POST'])
def signup():
    form = SignupForm(request.form)
    retry = False

    if request.method == 'POST' and form.validate():
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(name=username).first()

        if user is not None and user.verify_password(password):
            session['username'] = username
            session['user_id'] = user.id
            message_suscess = 'Bienvenido {}'.format(session['username'])
            flash(message_suscess)
            return redirect( url_for('index') )
            
        else:
            message = 'Usuario o password invalida'
            retry = True
            # flash(message)

    return render_template('signup.html', form=form, retry=retry)


@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username')

    return redirect(url_for('signup'))   # Se coloca la funcion a la que quiero usar como redireccion
        

@app.route('/login', methods=['GET','POST'])
def login():
    login_form = LoginForm(request.form)

    if request.method == 'POST' and login_form.validate():
        
        user = User(
            login_form.username.data,
            login_form.password.data,
            login_form.email.data
        )    

        @copy_current_request_context
        def send_message(email, username):
            send_email(email, username)
        
        sender = threading.Thread(name='mail_sender', 
                                        target=send_message,
                                        args = (login_form.email.data, login_form.username.data))
        sender.start()

        try:
            
            db.session.add(user)
            db.session.commit()
            
            

            


            flash('Success adding user')

            session['username'] = login_form.username.data
            session['user_id'] = user.id
            message_suscess = 'Bienvenido {}'.format(session['username'])
            flash(message_suscess)


            return redirect( url_for('index') )
            
        except Exception as e:
            flash_message = 'Error adding user {}'.format(e)
            flash(flash_message)

    return render_template('login.html', form=login_form)


@app.route('/cookie')
def cookie():
    response = make_response( render_template('cookie.html') )
    response.set_cookie('custome_cookie', 'Cesar_cookie')
    return response


@app.route('/comment', methods=['GET','POST'])
def comment():
    
    form = CommentForm(request.form)  # Si el cliente no ha enviado info, se va a crear una instancia nueva, de lo contratio se va a crear con la info enviada
    
    if request.method == 'POST' and form.validate():
        comentario = Comment(user_id=session['user_id'] , comment=form.comment.data)
        
        try:
            db.session.add(comentario)
            db.session.commit()
        except Exception as e:
            flash_message = 'Error adding comment {}'.format(e)
            flash(flash_message)
    
    elif request.method == 'POST' and form.validate() == False:
        print('Error en el formulario')

    form.comment.data = ""
    return render_template('comments.html', form=form)


@app.route('/', methods=['GET','POST'])
def index():
    #Cookie
    # custom_cookie = request.cookies.get('custome_cookie', 'No hay cookie')
    # print(custom_cookie)

    #Session
    if 'username' in session:
        username = session['username']
        print('El usuario tiene una session con el nombre de:',session['username'])
    else:
        username = 'None'

    return render_template('index.html', username=username)


@app.route('/ajax-login', methods=['POST'])
def ajax_login():
    print(request.form)
    username = request.form['username']
    response_dict = {'status':200,'username': 'cesar', 'id':'1'}
    response = json.dumps(response_dict)
    return response

if __name__ == '__main__':
    #my_db = DeveloperConfig()
    #Base, engine = my_db.start_db()
    db.init_app(app)
    mail.init_app(app)
    with app.app_context():
        db.create_all()
    #Base.metadata.create_all(engine)
    csrf.init_app(app)
    app.run() #Hacer cambio y que el servidor se reinicie automaticamente 