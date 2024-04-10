from extensions.extension import db
import uuid

# form defaults
def generate_uuid():
    return str(uuid.uuid4())
# playlists
class Playlist(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=generate_uuid, unique=True)
    title = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
    hits = db.Column(db.Integer, default=0)
    songs = db.relationship('Song', secondary='playlist_songs', backref='playlists')

playlist_songs = db.Table('playlist_songs',
    db.Column('playlist_id', db.String(36), db.ForeignKey('playlist.id'), primary_key=True),
    db.Column('song_id', db.String(36), db.ForeignKey('song.id'), 
    primary_key=True)
)