from flask_restx import Namespace, Resource
from flask import request
from models.album_model import Album
from models.song_model import Song
from extensions.extension import db
from api.api_models import album_output_model, album_input_model, output_all_songs
from decorator.decorator import auth_required, roles_accepted
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
'''
+--------------------------------------------------------------+
|                         namespace albums                     |
+--------------------------------------------------------------+
'''
ns_album = Namespace('albums', description='Album related operations')

#------------------------------------/albums/<string:id>---------------------------------#
@ns_album.route('/albums/<string:id>')
class AlbumApi(Resource):
    @ns_album.marshal_with(album_output_model)
    def get(self, id):
        album = Album.query.get(id)
        return album, 200
    
    @ns_album.expect(album_input_model)
    @ns_album.marshal_with(album_output_model)
    def post(self, id):
        title = request.json.get('title')
        release_year = request.json.get('release_year')
        album = Album(title=title, release_year=release_year, user_id=id)
        db.session.add(album)
        db.session.commit()
        return album, 201
    
    @ns_album.marshal_with(album_output_model)
    def delete(self, id):
        album = Album.query.get(id)
        db.session.delete(album)
        db.session.commit()
        return Album.query.get(id), 204
    
    @ns_album.expect(album_input_model)
    @ns_album.marshal_with(album_output_model)
    def put(self, id):
        album = Album.query.get(id)
        title = request.json.get('title')
        release_year = request.json.get('release_year')
        album.title = title
        album.release_year = release_year
        db.session.commit()
        return album, 200

#------------------------------------/albums/<string:id>/songs---------------------------------#
@ns_album.route('/albums/<string:id>/songs')
class AlbumSongsApi(Resource):
    @ns_album.marshal_with(output_all_songs)
    def get(self, id):
        album = Album.query.get(id)
        if not album:
            return {'error': 'Album not found'}, 404
        songs = album.songs
        return songs, 200

#-------------------------/albums/<string:id>/songs/<string:song_id>--------------------------#
@ns_album.route('/albums/<string:id>/songs/<string:song_id>')
class AlbumSongApi(Resource):
    @ns_album.marshal_with(output_all_songs)
    def get(self, id, song_id):
        album = Album.query.get(id)
        if not album:
            return {'error': 'Album not found'}, 404
        
        # get method use nhi kr skte sql-alch relationship me 
        # ye dict like obj k liye hota h tmhare pas list like obj h
        
        song = None 
        for s in album.songs:
            if s.id == song_id:
                song = s
        if song:
            return song 
        else:
            return {"message": "Song not found"}, 404
        
    @ns_album.marshal_with(output_all_songs)
    def post(self, id, song_id):
        album = Album.query.get(id)
        if not album:
            return {'error': 'Album not found'}, 404
        
        song = Song.query.get(song_id)
        if not song:
            return {'error': 'Song not found'}, 404

        album.songs.append(song)
        db.session.commit()

        return song, 201
        
    def delete(self, id, song_id):
        album = Album.query.get(id)
        if not album:
            return {'error': 'Album not found'}, 404
        print('now in the api delete method found the album')
        song = None 
        for s in album.songs:
            if s.id == song_id:
                song = s
        if song:
            print('now in the api delete method found the song...')
            album.songs.remove(song)
            # db.session.delete(song) pura song object ko hi delete kr deta h bhaii... bach k
            db.session.commit()
            return {"message": "Song deleted"}, 204
        else:
            print('now in the api delete method not found the song...')
            return {"message": "Song not found"}, 404
        

    @ns_album.expect(album_input_model)
    @ns_album.marshal_with(album_output_model)
    def put(self, id):
        album = Album.query.get(id)
        if album is None:
            return {'error': 'Album not found'}, 404

        data = request.json
        title = data.get('title')
        if title:
            album.title = title
            db.session.commit()
            return album, 200
        else:
            return {'error': 'No title provided'}, 400

#------------------------------------/albums/-------------------------------------#
@ns_album.route('/albums/')
class AlbumsListApi(Resource):
    @ns_album.marshal_with(album_output_model)
    @jwt_required()
    def get (self):
        album = Album.query.all()
        return album, 200
