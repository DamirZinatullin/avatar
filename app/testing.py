from app import db
from models import Suit, Fabric

suits = Suit.query.all()
for suit in suits:
    print(suit)