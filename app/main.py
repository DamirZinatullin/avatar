from app import app
from app import db
from suits.blueprint import suits
import view

app.register_blueprint(suits, url_prefix='/suits')
if __name__ == '__main__':
    app.run()
