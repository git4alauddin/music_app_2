from flask_restx import Namespace, Resource
from flask import request, jsonify
from models.user_model import User, Role
from werkzeug.security import check_password_hash, generate_password_hash
from api.api_models import user_login_model, user_register_model
# from flask_security import login_user, current_user, logout_user, auth_required, roles_accepted
from extensions.extension import db
# from models.user_model import user_datastore

import bcrypt
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

ns_auth = Namespace('auth', description='Authentication related operations')

@ns_auth.route('/login')
class LoginApi(Resource):
    @ns_auth.expect(user_login_model)
    def post(self):
        email = request.json.get('email')
        password = request.json.get('password')
        print(email, password)
        user = User.query.filter_by(email=email).first()
        # user = user_datastore.find_user(email=email)
        if user and bcrypt.checkpw(password.encode('utf-8'), user.password):
            # login_user(user)
            return {"token": create_access_token(identity=user.id, additional_claims={"role": user.role[0].name}), "email": user.email, "role": user.roles[0].name , "id":user.id, 'message': 'User logged in'}, 200
        else:
            return {'message': 'Invalid username or password'}, 401
        
@ns_auth.route('/test')
class TestApi(Resource):
    # @auth_required('token')
    # @roles_accepted('user')
    def get(self):
        return {'message': 'current_user.id'}, 200
        
@ns_auth.route('/logout')
class LogoutApi(Resource):
    def get(self):
        # logout_user()
        return {'message': 'User logged out'}, 200


@ns_auth.route('/register')
class RegisterApi(Resource):
    @ns_auth.expect(user_register_model)
    def post(self):
        username = request.json.get('username')
        email = request.json.get('email')
        password = request.json.get('password')

        if User.query.filter_by(email=email).first():
            return {'message': 'User already exists'}, 409
        else:
            hashed_password = bcrypt.hash_password(password.encode('utf-8'))
            # user_datastore.create_user(username=username, email=email, password=hashed_password, roles = ['user'])
            new_user = User(username=username, email=email, password=hashed_password)
            db.session.add(new_user)
            user_role = Role.query.filter_by(name='user').first()  # assuming 'user' role exists
            if user_role:
                new_user.roles.append(user_role)
            db.session.commit()

            return {'messgae': 'User created'}, 201  # Assuming user.to_dict() returns a JSON serializable representation of the user



    