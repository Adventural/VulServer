from app import db

class User(db.Model):
    __tablename__ = 'user'

    uid = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    username = db.Column(db.String(256), unique=True)
    password = db.Column(db.String(256))

    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username