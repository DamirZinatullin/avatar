from wtforms import Form, StringField, TextAreaField

class SuitForm(Form):
    title = StringField('title')
    data = StringField('data')