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


class Scenario(db.Model):
    __tablename__ = 'scenario'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), index=True, unique=True)
    description = db.Column(db.Text())
    creation_date = db.Column(db.DateTime())
    update_date = db.Column(db.DateTime())
    last_run = db.Column(db.DateTime())
    test = db.relationship("Test")


class Test(db.Model):
    """Create a test table."""
    __tablename__ = 'test'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), index=True, unique=True)
    test_type = db.Column(db.String(60))
    data = db.Column(db.Text())
    execute_date = db.Column(db.DateTime())
    scenario_id = db.Column(db.Integer, db.ForeignKey('scenario.id'))
    result = db.relationship("Result")
    group = db.relationship('Group')

class Group(db.Model):
    """Create a test table."""
    __tablename__ = 'group'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), index=True)
    spec_id = db.Column(db.Integer, db.ForeignKey('specification.id'))
    test_id = db.Column(db.Integer, db.ForeignKey('test.id'))


class Specification(db.Model):
    """Create a user table."""
    __tablename__ = 'specification'

    id = db.Column(db.Integer, primary_key=True)
    spec_name = db.Column(db.String(60), index=True, unique=True)
    url = db.Column(db.Text())
    group = db.relationship('Group')


class Result(db.Model):
    """Create a user table."""
    __tablename__ = 'result'

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(60))
    timestamp = db.Column(db.DateTime())
    spec_name = db.Column(db.String(60))
    time = db.Column(db.Integer)
    test_id = db.Column(db.Integer, db.ForeignKey('test.id'))


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
