# imports
from flask import Flask 
from flask_cors import CORS
from extensions.extension import api, db
# from flask_security import Security
from configs.config import DevelopmentConfig
# from models.user_model import user_datastore
from datetime import timedelta
from flask_jwt_extended import JWTManager
from cache import cache

# import resources
from api.auth_resource import ns_auth
from api.song_resource import ns_song
from api.playlist_resource import ns_playlist
from api.album_resource import ns_album
from api.user_resource import ns_user


from models.user_model import create_user, create_role
from sec import bcrypt

# initialize app
app = Flask(__name__)
# CORS(app, origins="*", methods="*")
CORS(app, resources={r"/*": {"origins": "*"}}, methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])

app.config.from_object(DevelopmentConfig)

# initialize extensions
db.init_app(app)

# security = Security(app, user_datastore)
api.init_app(app)

jwt = JWTManager(app)



if jwt:
    print('jwt initialized')
bcrypt.init_app(app)

#cache
cache.init_app(app)

with app.app_context():
    db.create_all()
    create_role()
    create_user()

# register namespaces
api.add_namespace(ns_auth)
api.add_namespace(ns_song)
api.add_namespace(ns_playlist)
api.add_namespace(ns_album)
api.add_namespace(ns_user)


if __name__ == '__main__':
    app.run(debug=True)