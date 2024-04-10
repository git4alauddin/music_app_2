# imports
import uuid
from flask_security import UserMixin, RoleMixin, Security, SQLAlchemyUserDatastore
from extensions.extension import db

# form defaults
def generate_uuid():
    return str(uuid.uuid4())

# users
class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model, UserMixin):
    id = db.Column(db.String(36), primary_key=True, default=generate_uuid, unique=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)  
    fs_uniquifier = db.Column(db.String(255), unique=True, nullable=False)
    active = db.Column(db.Boolean(), default=True)  # 
    roles = db.relationship('Role', secondary='user_roles', backref=db.backref('users', lazy='dynamic'))

user_roles = db.Table('user_roles',
    db.Column('user_id', db.String(36), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
)

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
