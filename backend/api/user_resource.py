from flask_restx import Resource, Namespace
from models.user_model import User
from models.playlist_model import Playlist
from models.song_model import Song
from models.album_model import Album
from flask_security import current_user, auth_required, roles_accepted
from api.api_models import user_output_model, album_output_model,playlist_output_model, user_input_model, output_all_songs

from extensions.extension import db
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
        user.role = 'creator'
        db.session.commit()
        return user, 201
    
    @ns_user.marshal_with(user_input_model)
    def delete(self, id):
        user = User.query.get(id)
        user.role = 'user'
        db.session.commit()
        return user

#----------------------------------/users/<string:id>/playlists-------------------------------#
@ns_user.route('/users/<string:id>/playlists')
class UserPlaylistApi(Resource):
    @ns_user.marshal_with(playlist_output_model)
    def get(self, id):
        playlists = Playlist.query.filter_by(user_id=id).all()
        return playlists, 200

#----------------------------------/users/<string:id>/albums-------------------------------#
@ns_user.route('/users/<string:id>/albums')
class UserAlbumApi(Resource):
    @ns_user.marshal_with(album_output_model)
    def get(self, id):
        albums = Album.query.filter_by(user_id=id).all()
        return albums, 200

#----------------------------------/users/<string:id>/songs-------------------------------#  
@ns_user.route('/users/songs')
class UserSongApi(Resource):
    @ns_user.marshal_with(output_all_songs)
    @auth_required('token')
    @roles_accepted('user')
    def get(self):
        print(current_user.id)
        songs = Song.query.filter_by(creator_id=current_user.id).all()
        return songs, 200

#----------------------------------/users------------------------------------#
@ns_user.route('/users')
class UsersListApi(Resource):
    @ns_user.marshal_with(user_output_model)
    def get(self):
        user = User.query.all()
        return user, 200