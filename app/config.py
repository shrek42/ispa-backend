class Config:
    """General app configuration."""
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    CACHE_TYPE = "simple"
    JWT_AUTH_USERNAME_KEY = "email"
    JWT_AUTH_HEADER_PREFIX = "Token"
    JWT_HEADER_TYPE = "Token"
    ALLOWED_EXTENSIOS = {"txt", "pdf", "png", "jpg", "jpeg"}


class TestConfig(Config):
    """Test configuration."""
    DEBUG = True
    TESTING = True
    # database uri here


class DevConfig(Config):
    """Development configuration."""
    ENV = "dev"
    DEBUG = True


class ProdConfig(Config):
    """Production configuration."""
    # database uri here


app_config = {
    "testing": TestConfig,
    "development": DevConfig,
    "production": ProdConfig,
}
