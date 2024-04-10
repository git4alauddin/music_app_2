from flask_restx import Namespace, Resource
from flask import request, jsonify
from models.user_model import User
from werkzeug.security import check_password_hash, generate_password_hash
from api.api_models import user_login_model, user_register_model
from flask_security import login_user, current_user
from extensions.extension import db
from models.user_model import user_datastore


ns_auth = Namespace('auth')

@ns_auth.route('/login')
class LoginApi(Resource):
    @ns_auth.expect(user_login_model)
    def post(self):
        email = request.json.get('email')
        password = request.json.get('password')
        user = user_datastore.find_user(email=email)
        if user and check_password_hash(user.password, password):
            login_user(user)
            return {"token": user.get_auth_token(), "email": user.email, "role": user.roles[0].name , "id":user.id}, 200

        else:
            return {'message': 'Invalid username or password'}, 401

@ns_auth.route('/register')
class RegisterApi(Resource):
    @ns_auth.expect(user_register_model)
    def post(self):
        username = request.json.get('username')
        email = request.json.get('email')
        password = request.json.get('password')

        if user_datastore.find_user(email=email):
            return {'message': 'User already exists'}, 409
        else:
            hashed_password = generate_password_hash(password)
            user_datastore.create_user(username=username, email=email, password=hashed_password, roles = ['user'])
            db.session.commit()

            return {'messgae': 'User created'}, 201  # Assuming user.to_dict() returns a JSON serializable representation of the user
