from app import db
from datetime import datetime
import re


def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s)


suit_fabrics = db.Table('suit_fabrics',
                        db.Column('suit_id', db.Integer,
                                  db.ForeignKey('suit.id')),
                        db.Column('fabric_id', db.Integer,
                                  db.ForeignKey('fabric.id'))
                        )


class Suit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    data = db.Column(db.String(250))
    slug = db.Column(db.String(140), unique=True)
    created = db.Column(db.DateTime, default=datetime.now())
    price = db.Column(db.DECIMAL(9, 2))
    fabrics = db.relationship('Fabric', secondary=suit_fabrics,
                              backref=db.backref('suits', lazy='dynamic'))

    def __init__(self, *args, **kwargs):
        super(Suit, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return 'Suit id:{}, title: {}, price:{}'.format(self.suit_id,
                                                        self.title, self.price)


class Fabric(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    wool = db.Column(db.Integer)
    elastane = db.Column(db.Integer)
    polyester = db.Column(db.Integer)
    viscose = db.Column(db.Integer)
    flax = db.Column(db.Integer)
    cashmere = db.Column(db.Integer)
    cost = db.Column(db.DECIMAL(9, 2))

    def __init__(self, *args, **kwargs):
        super(Fabric, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)

    def __repr__(self):
        return 'Fabric id:{}, name: {}, cost:{}, wool: {}, elastane: {}'.format(
            self.id, self.name, self.cost, self.wool, self.elastane)
