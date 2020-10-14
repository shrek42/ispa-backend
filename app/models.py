from app.app import db


class User(db.Model):
    """Create a user table."""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), index=True, unique=True)
    email = db.Column(db.String(30), index=True, unique=True)
    password_hash = db.Column(db.Text())
    is_admin = db.Column(db.Boolean, default=False)
    used_keys = db.relationship('UsedKey', backref='user', lazy='dynamic')

    def __repr__(self):
        return '<User: {} with email: {}>'.format(self.username, self.email)
