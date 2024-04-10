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






