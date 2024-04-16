from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from functools import wraps
from models.user_model import User

# Custom decorator for authentication
def auth_required(fn):
    @wraps(fn)
    def decorated(*args, **kwargs):
        try:
            # Check for JWT token in request headers
            jwt_token = request.headers.get('Authorization').split()[1]
            # Verify JWT token
            get_jwt_identity(jwt_token)
            return fn(*args, **kwargs)
        except Exception as e:
            return jsonify({'message': 'Authentication required'}), 401
    return decorated

# Custom decorator for role-based access control
def roles_accepted(*roles):
    def decorator(fn):
        @wraps(fn)
        def decorated(*args, **kwargs):
            try:
                # Check if the current user has any of the required roles
                current_roles = get_current_user_roles()
                if any(role in current_roles for role in roles):
                    return fn(*args, **kwargs)
                else:
                    return jsonify({'message': 'Insufficient permissions'}), 403
            except Exception as e:
                return jsonify({'message': 'Authentication required'}), 401
        return decorated
    return decorator

# Example of getting current user's roles (you need to implement this)
def get_current_user_roles():
    # Get current user's roles from database or JWT token claims
    # Example implementation:
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    return [role.name for role in user.roles]


