from flask import Blueprint
from flask import render_template, request
from models import Suit, Fabric

suits = Blueprint('suits', __name__, template_folder='templates')


@suits.route('/')
def index():
    q = request.args.get('q')
    if q:
        suits = Suit.query.filter(Suit.title.contains(q)).all()
    else:
        suits = Suit.query.all()
    return render_template('/suits/index.html', suits=suits)


@suits.route('/<slug>')
def suit_detail(slug):
    suit = Suit.query.filter(Suit.slug == slug).first()
    fabrics = suit.fabrics
    return render_template('/suits/suit_detail.html', suit=suit,
                           fabrics=fabrics)
