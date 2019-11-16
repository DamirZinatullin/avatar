from app import db
from datetime import datetime
import re
from flask_security import UserMixin, RoleMixin


def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s)


# suit_fabrics = db.Table('suit_fabrics',
#                         db.Column('suit_id', db.Integer,
#                                   db.ForeignKey('suit.id')),
#                         db.Column('fabric_id', db.Integer,
#                                   db.ForeignKey('fabric.id'))
#                         )
#
# suit_tailors = db.Table('suit_tailors',
#                         db.Column('suit_id', db.Integer,
#                                   db.ForeignKey('suit.id')),
#                         db.Column('tailor_id', db.Integer,
#                                   db.ForeignKey('tailor.id'))
#                         )

# suit_consultants = db.Table('suit_consultants',
#                             db.Column('suit_id', db.Integer,
#                                       db.ForeignKey('suit.id')),
#                             db.Column('consultant_id', db.Integer,
#                                       db.ForeignKey('consultant.id'))
#                             )
#

class Suit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140), nullable=False)
    data = db.Column(db.String(250))
    slug = db.Column(db.String(140), unique=True)
    created = db.Column(db.DateTime, default=datetime.now())
    price = db.Column(db.DECIMAL(9, 2))
    fabric_id = db.Column(db.Integer, db.ForeignKey('fabric.id'))
    tailor_id = db.Column(db.Integer, db.ForeignKey('tailor.id'))
    consultant_id = db.Column(db.Integer, db.ForeignKey('consultant.id'))
    garment_id = db.Column(db.Integer, db.ForeignKey('garment.id'))
    scan_id = db.Column(db.Integer, db.ForeignKey('scan.id'))
    status_id = db.Column(db.Integer, db.ForeignKey('status.id'))
    kit_id = db.Column(db.Integer, db.ForeignKey('kit.id'))
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    priority_id = db.Column(db.Integer, db.ForeignKey('priority.id'))

    def __init__(self, *args, **kwargs):
        super(Suit, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return 'Suit id:{}, title: {}, price:{}, fabric:{}, slug:{}'.format(
            self.id,
            self.title, self.price, self.fabric, self.slug)


class Fabric(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    wool = db.Column(db.Integer)
    slug = db.Column(db.String(140), unique=True)
    elastane = db.Column(db.Integer)
    polyester = db.Column(db.Integer)
    viscose = db.Column(db.Integer)
    flax = db.Column(db.Integer)
    cashmere = db.Column(db.Integer)
    cost = db.Column(db.DECIMAL(9, 2))
    suits = db.relationship('Suit', backref='fabric')

    def __init__(self, *args, **kwargs):
        super(Fabric, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)

    def __repr__(self):
        return 'Fabric id:{}, name: {}, cost:{}, wool: {},' \
               ' elastane:{} '.format(self.id, self.name, self.cost, self.wool,
                                      self.elastane)


class Garment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    suits = db.relationship('Suit', backref='garment')

    def __init__(self, *args, **kwargs):
        super(Garment, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)

    def __repr__(self):
        return 'Garment id:{}, name: {}'.format(
            self.id, self.name)


class Scan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    height = db.Column(db.DECIMAL(9, 2))
    weight = db.Column(db.DECIMAL(9, 2))
    date = db.Column(db.DateTime, default=datetime.now())
    data = db.Column(db.Text)
    suits = db.relationship('Suit', backref='scan')

    def __init__(self, *args, **kwargs):
        super(Scan, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)

    def __repr__(self):
        return 'Scan id:{}, data: {}'.format(
            self.id, self.data)


class Tailor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    surname = db.Column(db.String(140))
    patronymic = db.Column(db.String(140))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(140))
    date = db.Column(db.DateTime, default=datetime.now())
    suits = db.relationship('Suit', backref='tailor')

    def __init__(self, *args, **kwargs):
        super(Tailor, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)

    def __repr__(self):
        return 'Tailor id:{}, name: {}, surname: {}'.format(
            self.id, self.name, self.surname)


class Consultant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    surname = db.Column(db.String(140))
    patronymic = db.Column(db.String(140))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(140))
    date = db.Column(db.DateTime, default=datetime.now())
    suits = db.relationship('Suit', backref='consultant')

    def __init__(self, *args, **kwargs):
        super(Consultant, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)

    def __repr__(self):
        return 'Consultant id:{}, name: {}, surname: {}'.format(
            self.id, self.name, self.surname)


class Status(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    suits = db.relationship('Suit', backref='status')
    orders = db.relationship('Order', backref='status')

    def __init__(self, *args, **kwargs):
        super(Status, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)

    def __repr__(self):
        return 'Status id:{}, name: {}'.format(self.id, self.name)


class Kit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    suits = db.relationship('Suit', backref='kit')

    def __init__(self, *args, **kwargs):
        super(Status, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)

    def __repr__(self):
        return 'Kit id:{}'.format(self.id)


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    create_date = db.Column(db.DateTime, default=datetime.now())
    closing_date = db.Column(db.DateTime)
    status_id = db.Column(db.Integer, db.ForeignKey('status.id'))
    price = db.Column(db.DECIMAL(9, 2))
    suits = db.relationship('Suit', backref='order')

    def __init__(self, *args, **kwargs):
        super(Order, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)

    def __repr__(self):
        return 'Order id:{}'.format(self.id)


class Priority(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    suits = db.relationship('Suit', backref='priority')

    def __init__(self, *args, **kwargs):
        super(Priority, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)

    def __repr__(self):
        return 'Priority id:{}, priority name: {}'.format(self.id, self.name)


### Flask Security

roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer(),
                                 db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer(),
                                 db.ForeignKey('role.id')))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(255))
