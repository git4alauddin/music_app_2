from extensions.extension import api 
from flask_restx import fields


# auth
user_login_model = api.model("UserLogin", {
    "email": fields.String,
    "password": fields.String
})


user_register_model = api.model("UserRegister", {
    "username": fields.String,
    "email": fields.String,
    "password": fields.String
})


# songs
upload_song_model = api.model("UploadSong", {
    "title": fields.String,
    "artist": fields.String,
    "genre": fields.String,
    "lyrics": fields.String,
    "audio_file": fields.Raw
})

output_all_songs = api.model("AllSongs", {
    "id": fields.String,
    "creator_id": fields.String,
    "title": fields.String,
    "artist": fields.String,
    "genre": fields.String,
    "lyrics": fields.String,
    "average_rating": fields.Float,
    "is_flagged": fields.Boolean
})


# playlist
playlist_output_model = api.model("Playlist", {
    "id": fields.String,
    "title": fields.String,
    "user_id": fields.String
})

playlist_input_model = api.model("PlaylistInput", {
    "id": fields.String,
    "title": fields.String
})


# album
album_output_model = api.model("Album", {
    "id": fields.String,
    "title": fields.String,
    "user_id": fields.String,
    "release_year": fields.Integer

})

album_input_model = api.model("AlbumInput", {
    "id": fields.String,
    "title": fields.String,
    "release_year": fields.Integer
})


# user
user_output_model = api.model("User", {
    "id": fields.String,
    "username": fields.String,
    "roles": fields.List(fields.String),
    "email": fields.String,
    "active": fields.Boolean
})

user_input_model = api.model("UserInput", {
    "id": fields.String(required=True, description="User ID")
})

# rating
rating_input_model = api.model("RatingInput", {
    "value": fields.Integer,
    "song_id": fields.String
})


# stats
admin_stats_output_model = api.model("AdminStats", {
    "total_users": fields.Integer,
    "total_songs": fields.Integer,
    "total_playlists": fields.Integer,
    "total_albums": fields.Integer  
})

creator_stats_output_model = api.model("CreatorStats", {
    "total_songs": fields.Integer,
    "total_albums": fields.Integer,
    "total_playlists": fields.Integer,
    "average_rating": fields.Float
})