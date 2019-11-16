from app import db
# from models import Suit, Fabric, User
#
#
# suits = Suit.query.all()
# for suit in suits:
#     print(suit)
#
# users = User.query.all()
# for user in users:
#     print(user.email, user.password)
for i in dir(db):
    print(i)