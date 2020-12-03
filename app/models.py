from werkzeug.security import check_password_hash, generate_password_hash

from app.app import db


class User(db.Model):
    """Create a user table."""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    password_hash = db.Column(db.Text())

    @property
    def password(self):
        """Prevent password from being accessed."""
        raise AttributeError('Password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """Create password hash."""
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """Check if hashed password matches actual password."""
        return check_password_hash(self.password_hash, password)

    @classmethod
    def find_user_in_db(cls, email):
        return User.query.filter_by(email=email).first()

    def __repr__(self):
        return '<User: {} with email: {}>'.format(self.username, self.email)


class OldTokenModel(db.Model):
    """
    Model for revoked tokens.
    """
    __tablename__ = 'old_tokens'
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(120))

    def add(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def is_jti_blacklisted(cls, jti):
        query = cls.query.filter_by(jti=jti).first()
        return bool(query)
