from flask import Flask, render_template
from flask_wtf import FlaskForm, widgets
from wtforms import SelectMultipleField

SECRET_KEY = 'development'

app = Flask(__name__)
app.config.from_object(__name__)
from forms import ManSuitConstructorForm

form = ManSuitConstructorForm()
field = form.type_of_trousers
for i in dir(field):
    print(i)




#
# @app.route('/', methods=['post', 'get'])
# def hello_world():
#     form = SimpleForm()
#     if form.validate_on_submit():
#         print(form.example.data)
#     else:
#         print(form.errors)
#     return render_template('example.html', form=form)
#
#
# if __name__ == '__main__':
#     app.run(debug=True, port=1141)
