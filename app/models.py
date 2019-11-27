from app import db
from datetime import datetime
import re
from flask_security import UserMixin, RoleMixin


def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s)


class Suit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140), nullable=False)
    data = db.Column(db.String(250))
    slug = db.Column(db.String(140), unique=True)
    created = db.Column(db.DateTime, default=datetime.now())
    price = db.Column(db.DECIMAL(9, 2))
    fabric_id = db.Column(db.Integer, db.ForeignKey('fabric.id'))
    tailor_id = db.Column(db.Integer, db.ForeignKey('tailor.id'))
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
    color_id = db.Column(db.Integer, db.ForeignKey('color.id'))
    pattern_id = db.Column(db.Integer, db.ForeignKey('pattern.id'))
    price_bracket_id = db.Column(db.Integer, db.ForeignKey('price_bracket.id'))
    suits = db.relationship('Suit', backref='fabric')

    def __init__(self, *args, **kwargs):
        super(Fabric, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)

    def __repr__(self):
        return 'Fabric id:{}, name: {}, cost:{}, wool: {},' \
               ' elastane:{} '.format(self.id, self.name, self.cost, self.wool,
                                      self.elastane)


class Color(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    fabrics = db.relationship('Fabric', backref='color')

    def __init__(self, *args, **kwargs):
        super(Color, self, *args, **kwargs).__init__(*args, **kwargs)
        self.slug = slugify(self.name)

    def __repr__(self):
        return 'Color id: {}, name: {}'.format(self.id, self.name)


class Pattern(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    fabrics = db.relationship('Fabric', backref='pattern')

    def __init__(self, *args, **kwargs):
        super(Pattern, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)

    def __repr__(self):
        return 'Pattern id:{}, name: {}'.format(
            self.id, self.name)


class PriceBracket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    fabrics = db.relationship('Fabric', backref='price_bracket')

    def __init__(self, *args, **kwargs):
        super(PriceBracket, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)

    def __repr__(self):
        return 'Price_bracket id:{}, name: {}'.format(
            self.id, self.name)


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
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
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
    status_id = db.Column(db.Integer, db.ForeignKey('status.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))

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
    shop_id = db.Column(db.Integer, db.ForeignKey('shop.id'))
    status_id = db.Column(db.Integer, db.ForeignKey('status.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    date = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, *args, **kwargs):
        super(Consultant, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)

    def __repr__(self):
        return 'Consultant id:{}, name: {}, surname: {}'.format(
            self.id, self.name, self.surname)


class Manager(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    surname = db.Column(db.String(140))
    patronymic = db.Column(db.String(140))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(140))
    status_id = db.Column(db.Integer, db.ForeignKey('status.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    date = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, *args, **kwargs):
        super(Manager, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)

    def __repr__(self):
        return 'Manager id:{}, name: {}, surname: {}'.format(
            self.id, self.name, self.surname)


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    surname = db.Column(db.String(140))
    patronymic = db.Column(db.String(140))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(140))
    date = db.Column(db.DateTime, default=datetime.now())
    status_id = db.Column(db.Integer, db.ForeignKey('status.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    scans = db.relationship('Scan', backref='customer')

    def __init__(self, *args, **kwargs):
        super(Customer, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)

    def __repr__(self):
        return 'Customer id:{}, name: {}, surname: {}'.format(
            self.id, self.name, self.surname)


class Status(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    suits = db.relationship('Suit', backref='status')
    orders = db.relationship('Order', backref='status')
    tailors = db.relationship('Tailor', backref='status')
    consultants = db.relationship('Consultant', backref='status')
    managers = db.relationship('Manager', backref='status')
    customers = db.relationship('Customer', backref='status')

    def __init__(self, *args, **kwargs):
        super(Status, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)

    def __repr__(self):
        return 'Status id:{}, name: {}'.format(self.id, self.name)


class Kit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    suit_id = db.Column(db.Integer, db.ForeignKey('suit.id'))

    def __init__(self, *args, **kwargs):
        super(Status, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)

    def __repr__(self):
        return 'Kit id:{}'.format(self.id)


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shop_id = db.Column(db.Integer, db.ForeignKey('shop.id'))
    create_date = db.Column(db.DateTime, default=datetime.now())
    closing_date = db.Column(db.DateTime)
    status_id = db.Column(db.Integer, db.ForeignKey('status.id'))
    price = db.Column(db.DECIMAL(9, 2))
    suits = db.relationship('Suit', backref='order')
    delivery_type_id = db.Column(db.Integer, db.ForeignKey('delivery_type.id'))

    def __init__(self, *args, **kwargs):
        super(Order, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)

    def __repr__(self):
        return 'Order id:{}'.format(self.id)


class DeliveryType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    orders = db.relationship('Order', backref='delivery_type')

    def __init__(self, *args, **kwargs):
        super(DeliveryType, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)

    def __repr__(self):
        return 'Delivery type id:{}, name: {}'.format(self.id, self.name)


class Priority(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    suits = db.relationship('Suit', backref='priority')

    def __init__(self, *args, **kwargs):
        super(Priority, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)

    def __repr__(self):
        return 'Priority id:{}, name: {}'.format(self.id, self.name)


class Shop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(40))
    address = db.Column(db.String(150))
    phone = db.Column(db.String(20))
    consultants = db.relationship('Consultant', backref='shop')
    orders = db.relationship('Order', backref='shop')

    def __init__(self, *args, **kwargs):
        super(Shop, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)

    def __repr__(self):
        return 'Shop id:{}, address: {}'.format(self.id, self.address)


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
    name = db.Column(db.String(60))
    surname = db.Column(db.String(60))
    phone = db.Column(db.String(20))
    active = db.Column(db.Boolean())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(255))
    tailors = db.relationship('Tailor', backref='role')
    consultants = db.relationship('Consultant', backref='role')
    managers = db.relationship('Manager', backref='role')
    customers = db.relationship('Customer', backref='role')
