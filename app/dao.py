from app.models import Category, Room, User, Invoice, Booking, UserRoleEnum
import hashlib
from app import app, db
from sqlalchemy import Column, String, Integer, Float, Boolean, ForeignKey, VARCHAR, DATETIME, Enum, DateTime
from flask_login import current_user
from sqlalchemy import Column, String, Integer, Float, Boolean, ForeignKey, VARCHAR, DATETIME, Enum, DateTime
import enum
def get_categories():
    return Category.query.all()


def query_single_room(page=None):
    s_room = Room.query.filter(Room.category_id == 1)
    if page:
        page = int(page)
        page_size = app.config["PAGE_SIZE"]
        start = (page - 1) * page_size

        return s_room.slice(start, start + page_size)

    return s_room.all()


def get_products(kw, cate_id, page=None):
    products = Room.query

    if kw:
        products = products.filter(Room.name.contains(kw))

    if cate_id:
        products = products.filter(Room.category_id.__eq__(cate_id))

    if page:
        page = int(page)
        page_size = app.config["PAGE_SIZE"]
        start = (page - 1) * page_size

        return products.slice(start, start + page_size)

    return products.all()


def count_single_room():
    return Room.query.filter(Room.category_id == 1).count()


def count_product():
    return Room.query.count()


def get_user_by_id(user_id):
    return User.query.get(user_id)


def auth_user(username, password):
    password = str(hashlib.md5(password.encode('utf-8')).hexdigest())

    return User.query.filter(User.user_name.__eq__(username), User.password.__eq__(password)).first()


def add_receipt(cart):

        a = Category(name='Phòng 3 ng', capacity='3')
        db.session.add(a)
        db.session.commit()
    # for c in cart.values():
    #     b = Booking(price=c['price'], invoice=i, room_id=c['id'])
    #     db.session.add(b)
    #
    #     db.session.commit()

        return True
