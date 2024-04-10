from flask_restx import Namespace, Resource
from flask import request
from api.api_models import upload_song_model
from random import random
from flask_security import current_user
from werkzeug.utils import secure_filename
import os
from flask import current_app
from extensions.extension import db
from models.song_model import Song, SongFile
import random

ns_song = Namespace('songs', description='Song related operations')


@ns_song.route('/upload_song')
class UploadSongApi(Resource):
    @ns_song.expect(upload_song_model)
    def post(self):
        title = request.json.get('title')
        artist = request.json.get('artist')
        genre = request.json.get('genre')
        lyrics = request.json.get('lyrics')

        # audio_file = request.files.get('audio_file')
        random_suffix = random.randint(0, 10000)

        creator_id = current_user.id
        # original_filename = secure_filename(audio_file.filename)
        # file_extension = original_filename.rsplit('.', 1)[1]
        file_extension = 'mp3'
        new_filename = f'{artist}_{title}_{random_suffix}.{file_extension}'

        audio_file_path = os.path.join(current_app.config['SONG_UPLOAD_FOLDER'], new_filename)
        # audio_file.save(audio_file_path)

        # song_object
        song = Song(
            title=title,
            artist=artist,
            genre=genre,
            lyrics=lyrics,
            creator_id=creator_id
        )
        
        try:
            db.session.add(song)
            db.session.commit()

            # add the song file
            song_file = SongFile(
                song_id = song.id,
                file_name = new_filename
            )

            db.session.add(song_file)
            db.session.commit()




        except Exception as e:
            db.session.rollback()
            return {'message': 'Something went wrong'}, 500
        
        return {'message': 'Song uploaded successfully'}, 201