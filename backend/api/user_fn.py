from flask_restx import Resource, Namespace
from models.user_model import User, Role, user_roles
from models.playlist_model import Playlist
from models.song_model import Song, Rating
from models.album_model import Album
# from flask_security import current_user, auth_required, roles_accepted
from api.api_models import user_output_model, album_output_model,playlist_output_model, user_input_model, output_all_songs, creator_stats_output_model, admin_stats_output_model
from sqlalchemy import func 
from extensions.extension import db
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required

ns_user = Namespace('userfn', description='User fn related operations')


from flask import request
# blacklist and whitelist user
ns_user.route('/blacklist')
class UserBlacklistApi(Resource):    
    # @auth_required('token')
    @jwt_required()
    def put(self):
        user = request.json.get('user_id')
        print(user)
        user.active = False
        db.session.commit()
        return {'message': 'User blacklisted'}
    
ns_user.route('/whitelist')
class UserWhitelistApi(Resource):
    # @auth_required('token')
    @jwt_required()
    def put(self):
        user = request.json.get('user_id')
        if user:
            print(user.to_dict())
            user.active = True
            db.session.commit()
            return {'message': 'User whitelisted'}
        return {'message': 'User not found'}