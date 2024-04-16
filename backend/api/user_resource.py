from flask_restx import Resource, Namespace
from models.user_model import User, Role
from models.playlist_model import Playlist
from models.song_model import Song, Rating
from models.album_model import Album
# from flask_security import current_user, auth_required, roles_accepted
from api.api_models import user_output_model, album_output_model,playlist_output_model, user_input_model, output_all_songs, creator_stats_output_model, admin_stats_output_model
from sqlalchemy import func 
from extensions.extension import db
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required

# current_user = get_jwt_identity()
# print(f'current_user: {current_user}')
'''
+--------------------------------------------------------------+
|                         namespace users                      |
+--------------------------------------------------------------+
'''
ns_user = Namespace('users', description='User related operations')

#---------------------------------/users/<string:id>-------------------------------#
@ns_user.route('/users/<string:id>')
class UserApi(Resource):
    @ns_user.marshal_with(user_input_model)
    def get(self, id):
        user = User.query.get(id)
        return user, 200
    
    @ns_user.expect(user_output_model)
    @ns_user.marshal_with(user_input_model)
    def put(self,id):
        user = User.query.get(id)
        new_role = Role.query.filter_by(name='creator').first()
        user.roles = [new_role]
        db.session.commit()
        return user, 201
    
    @ns_user.marshal_with(user_input_model)
    def delete(self, id):
        user = User.query.get(id)
        user.role = 'user'
        db.session.commit()
        return user

#----------------------------------/users/<string:id>/playlists-------------------------------#
@ns_user.route('/users/playlists')
class UserPlaylistApi(Resource):
    # @auth_required('token')
    # @roles_accepted('user', 'creator')
    @ns_user.marshal_with(playlist_output_model)
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        playlists = Playlist.query.filter_by(user_id=current_user['id']).all()
        return playlists, 200

#----------------------------------/users/<string:id>/albums-------------------------------#
@ns_user.route('/users/albums')
class UserAlbumApi(Resource):
    # @auth_required('token')
    # @roles_accepted('user', 'creator')
    @ns_user.marshal_with(album_output_model)
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        albums = Album.query.filter_by(user_id=current_user['id']).all()
        return albums, 200

#----------------------------------/users/<string:id>/songs-------------------------------#  
@ns_user.route('/users/songs')
class UserSongApi(Resource):
    @ns_user.marshal_with(output_all_songs)
    @jwt_required()
    # @auth_required('token')
    # @roles_accepted('user')
    def get(self):
        current_user = get_jwt_identity()
        songs = Song.query.filter_by(creator_id=current_user['id']).all()
        return songs, 200

#----------------------------------/users------------------------------------#
@ns_user.route('/users')
class UsersListApi(Resource):
    @ns_user.marshal_with(user_output_model)
    def get(self):
        user = User.query.all()
        return user, 200


# blacklist and whitelist user
ns_user.route('/users/blacklist/<string:user_id>')
class UserBlacklistApi(Resource):    
    # @auth_required('token')

    def put(self, user_id):
        user = User.query.get(user_id)
        user.active = False
        db.session.commit()
        return user
    
ns_user.route('/users/whitelist/<string:user_id>')
class UserWhitelistApi(Resource):
    # @auth_required('token')
    
    def put(self, user_id):
        user = User.query.get(user_id)
        user.active = True
        db.session.commit()
        return user

# -------------------stats---------------------------
@ns_user.route('/users/creator_stats')
class CreatorStatsApi(Resource):
    @jwt_required()
    @ns_user.marshal_with(creator_stats_output_model)
    def get(self):
        current_user = get_jwt_identity()
        total_songs = Song.query.filter_by(creator_id=current_user['id']).count()
        total_albums = Album.query.filter_by(user_id=current_user['id']).count()
        total_playlists = Playlist.query.filter_by(user_id=current_user['id']).count()

        average_rating = db.session.query(func.avg(Rating.value)).join(Song).filter(Song.creator_id == current_user['id']).scalar()
        average_rating = round(average_rating, 1) if average_rating else 0.0

        return {'total_songs': total_songs, 'total_albums': total_albums, 'total_playlists': total_playlists, 'average_rating': average_rating}
    

@ns_user.route('/users/admin_stats')
class AdminStatsApi(Resource):
   
    @ns_user.marshal_with(admin_stats_output_model)
    @jwt_required()
    def get(self):
        total_users = User.query.count()
        total_songs = Song.query.count()
        total_albums = Album.query.count()
        total_playlists = Playlist.query.count()

        return {'total_users': total_users, 'total_songs': total_songs, 'total_albums': total_albums, 'total_playlists': total_playlists}

    
