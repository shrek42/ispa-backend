from app.models import OldTokenModel
from flask_jwt_extended import JWTManager


class Jwt_Manager:
    """
    Class which is wrapper for Jwr Manager.
    """

    def __init__(self):
        self.app = None

    def init_jwt(self, app):
        self.app = app
        self.jwt = JWTManager(app)

    def delete_jti(self, jti):
        if not self.check_black_listed_jti(jti):
            old_token = OldTokenModel(jti=jti)
            old_token.add()
        else:
            raise Exception("Jti already BlacLister")

    def check_black_listed_jti(self, jti):
        return OldTokenModel.is_jti_blacklisted(jti)
