from flask_wtf import FlaskForm
from wtforms import Form, StringField, TextAreaField, DecimalField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo


class SuitForm(Form):
    title = StringField('title')
    data = StringField('data')
    price = DecimalField('price')


class RegisterForm(Form):
    name = StringField('name')
    surname = StringField('surname')
    city = StringField('city')
    phone = StringField('phone')
    email = StringField('email', validators=[DataRequired, Email])
    password = StringField('password')


class ManSuitConstructorForm(Form):
    type_of_trousers = SelectField('Тип брюк',
                                   choices=[('straight', 'Прямые'),
                                            ('skinny', 'Зауженные')])
    length_of_trousers = SelectField('Длина брюк', choices=[
        ('standart', 'Cтандартная длина'),
        ('oxford_trousers', 'Под оксфорды'), ('chelsea_trousers', 'Под челси'),
        ('lofer_trousers', 'Под лоферы')])
    silhouette_of_jacket = SelectField('Силуэт', choices=[
        ('straight', 'Прямой(классический)'), ('skinny', 'Зауженный'),
        ('fitted', 'Приталинный'), ('semi-fitted', 'Полуприталинный')])
    type_of_jacket = SelectField('Тип пиджака',
                                 choices=[('single_breasted', 'Однобортный'),
                                          ('double_breasted', 'Двубортный')])
    avatar_item = SelectField('Выбрать аватар',
                              choices=[(f'avatar_{i}', f'Аватар {i}') for i in
                                       range(1, 6)])
    # tissue_structure =
