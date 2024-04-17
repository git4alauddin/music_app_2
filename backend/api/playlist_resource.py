from flask_restx import Namespace, Resource
from flask import request
from models.playlist_model import Playlist 
from models.song_model import Song
from extensions.extension import db
from api.api_models import playlist_output_model, playlist_input_model, output_all_songs
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
'''
+--------------------------------------------------------------+
|                         namespace playlists                  |
+--------------------------------------------------------------+
'''
ns_playlist = Namespace('playlists', description='Playlist related operations')

#---------------------------------/playlists/<string:id>-------------------------------#
@ns_playlist.route('/playlists/<string:id>')
class PlaylistApi(Resource):
    @ns_playlist.marshal_with(playlist_output_model)
    @jwt_required()
    def get(self, id):
        playlist = Playlist.query.get(id)
        return playlist, 200
    
    @ns_playlist.expect(playlist_input_model)
    @ns_playlist.marshal_with(playlist_output_model)
    @jwt_required()
    def post(self, id):
        title = request.json.get('title')
        playlist = Playlist.query.filter_by(user_id = id).filter_by(title=title).first()
        if playlist:
            return {'error': 'Playlist title already exists'}, 400
        playlist = Playlist(title=title, user_id=id)
        db.session.add(playlist)
        db.session.commit()
        return {'message': 'Playlist created'}, 201
    
    @ns_playlist.marshal_with(playlist_output_model)
    @jwt_required()
    def delete(self, id):
        playlist = Playlist.query.get(id)
        db.session.delete(playlist)
        db.session.commit()
        return Playlist.query.get(id), 204
    
    @ns_playlist.expect(playlist_input_model)
    @ns_playlist.marshal_with(playlist_output_model)
    @jwt_required()
    def put(self, id):
        playlist = Playlist.query.get(id)
        title = request.json.get('title')
        if title:
            playlist.title = title
            db.session.commit()
            return playlist, 200
        else:
            return {'error': 'No title provided'}, 400

#----------------------------------/playlists/<string:id>/songs-------------------------------#
@ns_playlist.route('/playlists/<string:id>/songs')
class PlaylistSongsApi(Resource):
    @ns_playlist.marshal_with(output_all_songs)
    @jwt_required()
    def get(self, id):
        playlist = Playlist.query.get(id)
        if not playlist:
            return {'error': 'Playlist not found'}, 404
        songs = playlist.songs
        return songs, 200

#-----------------------------/playlists/<string:id>/songs/<string:song_id-----------------------------#
@ns_playlist.route('/playlists/<string:id>/songs/<string:song_id>')
class PlaylistSongApi(Resource):
    @ns_playlist.marshal_with(output_all_songs)
    @jwt_required()
    def get(self, id, song_id):
        playlist = Playlist.query.get(id)
        if not playlist:
            return {'error': 'Playlist not found'}, 404
        
        song = None 
        for s in playlist.songs:
            if s.id == song_id:
                song = s
        if song:
            return song, 200
        else:
            return {"message": "Song not found"}, 404
        
    @ns_playlist.marshal_with(output_all_songs)
    @jwt_required()
    def post(self, id, song_id):
        playlist = Playlist.query.get(id)
        if not playlist:
            return {'error': 'Playlist not found'}, 404
        
        song = Song.query.get(song_id)
        if not song:
            return {'error': 'Song not found'}, 404

        playlist.songs.append(song)
        db.session.commit()

        return song, 201

    @jwt_required()  
    def delete(self, id, song_id):
        playlist = Playlist.query.get(id)
        if not playlist:
            return {'error': 'Playlist not found'}, 404
        
        song = None 
        for s in playlist.songs:
            if s.id == song_id:
                song = s
        if song:
            playlist.songs.remove(song)
            db.session.commit()
            return {"message": "Song deleted"}, 204
        else:
            return {"message": "Song not found"}, 404
        

    @ns_playlist.expect(playlist_input_model)
    @ns_playlist.marshal_with(playlist_output_model)
    @jwt_required()
    def put(self, id):
        playlist = Playlist.query.get(id)
        if playlist is None:
            return {'error': 'Playlist not found'}, 404

        data = request.json
        title = data.get('title')
        if title:
            playlist.title = title
            db.session.commit()
            return playlist, 200
        else:
            return {'error': 'No title provided'}, 400

#----------------------------------/playlists/-----------------------------------#
@ns_playlist.route('/playlists')
class PlaylistsListApi(Resource):
    @ns_playlist.marshal_with(playlist_output_model)
    @jwt_required()
    def get (self):
        playlist = Playlist.query.all()
        return playlist, 200
    




