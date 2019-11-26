from wtforms import Form, StringField, TextAreaField, DecimalField


class SuitForm(Form):
    title = StringField('title')
    data = StringField('data')
    price = DecimalField('price')


class RegisterForm(Form):
    name = StringField('name')
    surname = StringField('surname')
    city = StringField('city')
    phone = StringField('phone')
    email = StringField('email')
    password = StringField('password')
