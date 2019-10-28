from app import app
from flask import render_template, request

from models import Suit, Fabric, Tailor
from forms import SuitForm
from app import db
from flask import redirect
from flask import url_for


@app.route('/create', methods=['POST', 'GET'])
def create_suit():
    if request.method == 'POST':
        title = request.form['title']
        data = request.form['data']

        try:
            suit = Suit(title=title, data=data)
            db.session.add(suit)
            db.session.commit()
        except:
            print('Something wrong')
        return redirect(url_for('index'))
    form = SuitForm()
    return render_template('create_suit.html', form=form)


@app.route('/')
def index():
    q = request.args.get('q')
    if q:
        suits = Suit.query.filter(Suit.title.contains(q)).all()
    else:
        suits = Suit.query.all()
    return render_template('index.html', suits=suits)


@app.route('/<slug>')
def suit_detail(slug):
    suit = Suit.query.filter(Suit.slug == slug).first()
    fabrics = suit.fabrics
    return render_template('suit_detail.html', suit=suit, fabrics=fabrics)


@app.route('/fabric/<slug>')
def fabric_detail(slug):
    fabric = Fabric.query.filter(Fabric.slug == slug).first()
    suits = fabric.suits.all()
    return render_template('fabric_detail.html', fabric=fabric, suits=suits)
