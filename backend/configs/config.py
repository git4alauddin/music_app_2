#-------------------base_config------------------#
class Config():
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///mad22.sqlite'
    SECRET_KEY = 'my_secret_key'

# env_development
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///11.sqlite'
    SECRET_KEY = 'my-very-secret-key'
    # HEADER FOR SECURITY
    SECURITY_TOKEN_AUTHENTICATION_HEADER = 'Authorization'

    SONG_UPLOAD_FOLDER = 'static/songs'
    
# env_production
class ProductionConfig(Config):
    pass