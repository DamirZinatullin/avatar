from app import app
from flask import render_template, request

from models import Suit, Fabric, Tailor


@app.route('/')
def index():
    q = request.args.get('q')
    if q:
        suits = Suit.query.filter(Suit.title.contains(q)).all()
        return render_template('/suits/index.html', suits=suits)
    else:
        return render_template('index.html')


@app.route('/fabric/<slug>')
def fabric_detail(slug):
    fabric = Fabric.query.filter(Fabric.slug == slug).first()
    suits = fabric.suits.all()
    return render_template('fabric_detail.html', fabric=fabric, suits=suits)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
