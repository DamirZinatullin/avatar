from flask import Blueprint
from flask import render_template, request, redirect, url_for
from app import db
from models import Suit, Fabric
from forms import SuitForm

from flask_security import login_required

suits = Blueprint('suits', __name__, template_folder='templates')


@suits.route('/')
def index():
    q = request.args.get('q')
    page = request.args.get('page')
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1
    if q:
        suits = Suit.query.filter(Suit.title.contains(q))  # .all()
    else:
        suits = Suit.query.order_by(Suit.created.desc())
    pages = suits.paginate(page=page, per_page=5)
    return render_template('/suits/index.html', pages=pages)


@suits.route('/create', methods=['POST', 'GET'])
@login_required
def create_suit():
    if request.method == 'POST':
        title = request.form['title']
        data = request.form['data']
        price = request.form['price']

        try:
            suit = Suit(title=title, data=data, price=price)
            db.session.add(suit)
            db.session.commit()
        except:
            print('Something wrong')
        return redirect(url_for('suits.index'))
    form = SuitForm()
    return render_template('suits/create_suit.html', form=form)


@suits.route('/<slug>/edit', methods=['POST', 'GET'])
@login_required
def edit_suit(slug):
    suit = Suit.query.filter(Suit.slug == slug).first_or_404()
    if request.method == "POST":
        form = SuitForm(formdata=request.form, obj=suit)
        form.populate_obj(suit)
        db.session.commit()
        return redirect(url_for('suits.suit_detail', slug=suit.slug))
    form = SuitForm(obj=suit)
    return render_template('suits/edit_suit.html', suit=suit, form=form)


@suits.route('/<slug>')
def suit_detail(slug):
    suit = Suit.query.filter(Suit.slug == slug).first_or_404()
    fabrics = suit.fabrics
    return render_template('/suits/suit_detail.html', suit=suit,
                           fabrics=fabrics)
