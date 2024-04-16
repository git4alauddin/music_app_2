from flask_restx import Namespace, Resource
from flask import request, jsonify
from models.user_model import User, Role
from api.api_models import user_login_model, user_register_model
from extensions.extension import db


import bcrypt
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required

ns_auth = Namespace('auth', description='Authentication related operations')

@ns_auth.route('/login')
class LoginApi(Resource):
    @ns_auth.expect(user_login_model)
    def post(self):
        email = request.json.get('email')
        password = request.json.get('password')
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.checkpw(password.encode('utf-8'), user.password):
            additional_claims = {"role": user.roles[0].name} if user.roles else {}
            token = create_access_token(identity=user.to_dict(), additional_claims=additional_claims)  # Pass user object as identity
            return {
                "token": token,
                "email": user.email,
                "role": user.roles[0].name if user.roles else None,
                "id": user.id,
                'message': 'User logged in'
            }, 200
        else:
            return {'message': 'Invalid username or password'}, 401

        
@ns_auth.route('/test')
class TestApi(Resource):
    def get(self):
        return {'message': 'current_user.id'}, 200
        
@ns_auth.route('/logout')
class LogoutApi(Resource):
    def get(self):
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
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            new_user = User(username=username, email=email, password=hashed_password)
            db.session.add(new_user)
            user_role = Role.query.filter_by(name='user').first()  # assuming 'user' role exists
            if user_role:
                new_user.roles.append(user_role)
            db.session.commit()

            return {'message': 'User created'}, 201
