from datetime import timedelta
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

    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)  \
    
    #cache
    CACHE_TYPE = 'RedisCache'
    CACHE_REDIS_HOST = 'localhost'
    CACHE_PORT = 6379
# a
class ProductionConfig(Config):
    pass