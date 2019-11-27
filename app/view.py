from app import app
from app import db
from flask import render_template, request, redirect, url_for
from forms import RegisterForm

from models import Suit, Fabric, Tailor, User


@app.route('/')
def index():
    q = request.args.get('q')
    if q:
        suits = Suit.query.filter(Suit.title.contains(q)).all()
        return render_template('/suits/index.html', suits=suits)
    else:
        return render_template('index.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        phone = request.form['phone']
        email = request.form['email']
        password = request.form['password']

        try:
            user = User(name=name, surname=surname, phone=phone, email=email,
                        password=password)
            db.session.add(user)
            db.session.commit()
        except:
            print('Something wrong')
        return redirect(url_for('index'))
    form = RegisterForm()
    return render_template('register.html', form=form)


@app.route('/fabric/<slug>')
def fabric_detail(slug):
    fabric = Fabric.query.filter(Fabric.slug == slug).first()
    suits = fabric.suits.all()
    return render_template('fabric_detail.html', fabric=fabric, suits=suits)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
