# imports
from flask import Flask 
from flask_cors import CORS
from extensions.extension import api, db
# from flask_security import Security
from configs.config import DevelopmentConfig
# from models.user_model import user_datastore
from datetime import timedelta
from flask_jwt_extended import JWTManager
from models.user_model import User

#celery
from worker import make_celery
from celery.schedules import crontab

#mail and cache
from cache import cache
from mail import mail
from flask_mail import Message

# import resources
from api.auth_resource import ns_auth
from api.song_resource import ns_song
from api.playlist_resource import ns_playlist
from api.album_resource import ns_album
from api.user_resource import ns_user


from models.user_model import create_user, create_role
from sec import bcrypt

# initialize app
app = Flask(__name__)
# CORS(app, origins="*", methods="*")
CORS(app, resources={r"/*": {"origins": "*"}}, methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])

app.config.from_object(DevelopmentConfig)

# initialize extensions
db.init_app(app)

# security = Security(app, user_datastore)
api.init_app(app)

jwt = JWTManager(app)



if jwt:
    print('jwt initialized')
bcrypt.init_app(app)

#cache
cache.init_app(app)

# mail
mail.init_app(app)

# celery
celery = make_celery(app)


# -------------------------celery tasks------------------------------#
def send_reminder(user):
    with mail.connect() as conn:
        msg = Message(subject='Reminder', sender='divyanshdixit0902@gmail.com', recipients=[user.email])
        msg.body = f'Hello {user.username},\n\nPlease visit my site.. you would love that!!'


def setup_periodic_tasks(sender, **kwargs):
    # sender.add_periodic_task(crontab(hour=5, minute=14), send_monthly_report.s())
    sender.add_periodic_task(crontab(hour=17, minute=1), visit_reminder.s())

@celery.task()
def visit_reminder():
    users = User.query.all()
    for user in users:
        send_reminder(user)
    return f'Reminder sent to {len(users)} users'
# -------------------------celery tasks------------------------------#

with app.app_context():
    db.create_all()
    create_role()
    create_user()

# register namespaces
api.add_namespace(ns_auth)
api.add_namespace(ns_song)
api.add_namespace(ns_playlist)
api.add_namespace(ns_album)
api.add_namespace(ns_user)


if __name__ == '__main__':
    app.run(debug=True)