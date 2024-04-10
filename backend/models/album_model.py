from extensions.extension import db
import uuid

# form defaults
def generate_uuid():
    return str(uuid.uuid4())

# albums
class Album(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=generate_uuid, unique=True)
    title = db.Column(db.String(100), nullable=False)
    release_year = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
    hits = db.Column(db.Integer, default=0)
    songs = db.relationship('Song', secondary='album_songs', backref='albums')

album_songs = db.Table('album_songs',
    db.Column('album_id', db.String(36), db.ForeignKey('album.id'), primary_key=True),
    db.Column('song_id', db.String(36), db.ForeignKey('song.id'), primary_key=True)
)