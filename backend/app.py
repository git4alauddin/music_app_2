# imports
from flask import Flask 
from flask_cors import CORS
from extensions.extension import api, db
from flask_security import Security
from configs.config import DevelopmentConfig
from models.user_model import user_datastore

# import resources
from api.auth_resource import ns_auth
from api.song_resource import ns_song
from api.playlist_resource import ns_playlist
from api.album_resource import ns_album
from api.user_resource import ns_user


# initialize app
app = Flask(__name__)
CORS(app)
app.config.from_object(DevelopmentConfig)

# initialize extensions
db.init_app(app)

security = Security(app, user_datastore)
api.init_app(app)



# register namespaces
api.add_namespace(ns_auth)
api.add_namespace(ns_song)
api.add_namespace(ns_playlist)
api.add_namespace(ns_album)
api.add_namespace(ns_user)


if __name__ == '__main__':
    app.run(debug=True)