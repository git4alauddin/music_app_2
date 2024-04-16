# imports
import uuid
# from flask_security import UserMixin, RoleMixin, Security, SQLAlchemyUserDatastore
from extensions.extension import db
from sec import bcrypt

# form defaults
def generate_uuid():
    return str(uuid.uuid4())

# users
class Role(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=generate_uuid, unique=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)  
    # fs_uniquifier = db.Column(db.String(255), unique=True, nullable=False)
    active = db.Column(db.Boolean(), default=True)  # 
    roles = db.relationship('Role', secondary='user_roles', backref=db.backref('users', lazy='dynamic'))

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }
    
user_roles = db.Table('user_roles',
    db.Column('user_id', db.String(36), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
)



# user_datastore = SQLAlchemyUserDatastore(db, User, Role)

def create_role():
    admin = Role.query.filter_by(name='admin').first()
    user = Role.query.filter_by(name='user').first()
    creator = Role.query.filter_by(name='creator').first()
    if not admin and not user and not creator:
        admin = Role(name='admin', description='admin role')
        user = Role(name='user', description='user role')
        creator = Role(name='creator', description='creator role')
        db.session.add(admin)
        db.session.add(user)
        db.session.add(creator)
        db.session.commit()

def create_user():
    admin = User.query.filter_by(email='admin@gmail.com').first()
    admin_role = Role.query.filter_by(name='admin').first()
    user = User.query.filter_by(email='user1@gmail.com').first()
    user_role = Role.query.filter_by(name='user').first()
    if not admin and not user and admin_role and user_role:
        admin = User(username='admin1', email='admin@gmail.com', password=bcrypt.generate_password_hash('admin123'))
        db.session.add(admin)
        admin.roles.append(admin_role)
        user1 = User(username='user1', email='user1@gmail.com', password=bcrypt.generate_password_hash('12345678'))
        db.session.add(user1)
        user1.roles.append(user_role)
        db.session.commit()