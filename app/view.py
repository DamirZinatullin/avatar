from app import app
from app import db
from flask import render_template, request, redirect, url_for, make_response
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


@app.route('/city/<city>', methods=['POST', 'GET'])
def set_city(city):
    city_dict = {'msc': 'Москва', 'spb': 'Санкт-Петербург',
                 'ekb': 'Екатеринбург'}
    res = make_response(redirect('/'))
    if city_dict.get(city):
        res.set_cookie('city', city_dict.get(city))
    return res


@app.route('/shipping_and_payment')
def shipping_and_payment():
    return render_template('shipping_and_payment.html')


@app.route('/addresses')
def addresses():
    return render_template('addresses.html')


@app.route('/fabric/<slug>')
def fabric_detail(slug):
    fabric = Fabric.query.filter(Fabric.slug == slug).first()
    suits = fabric.suits.all()
    return render_template('fabric_detail.html', fabric=fabric, suits=suits)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
