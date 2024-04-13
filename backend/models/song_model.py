from extensions.extension import db
import uuid

# form defaults
def generate_uuid():
    return str(uuid.uuid4())

# songs
class Song(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=generate_uuid, unique=True)
    title = db.Column(db.String(100), nullable=False)
    artist = db.Column(db.String(100), nullable=False)
    lyrics = db.Column(db.Text)
    genre = db.Column(db.String(50))
    hits = db.Column(db.Integer, default=0)
    creator_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
    average_rating = db.Column(db.Float, default=0.0)
    ratings = db.relationship('Rating', backref='song', lazy=True)
    is_flagged = db.Column(db.Boolean, default=False)


# song_files
class SongFile(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=generate_uuid, unique=True)
    song_id = db.Column(db.Integer, db.ForeignKey('song.id'), nullable=False)
    file_name = db.Column(db.String(255), nullable=False)


# ratings
class Rating(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=generate_uuid, unique=True)
    value = db.Column(db.Integer, nullable=False)
    song_id = db.Column(db.String(36), db.ForeignKey('song.id'), nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
