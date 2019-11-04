from wtforms import Form, StringField, TextAreaField, DecimalField

class SuitForm(Form):
    title = StringField('title')
    data = StringField('data')
    price = DecimalField('price')