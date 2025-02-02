# auth.py
from functools import wraps
from flask import request, jsonify

ROLE_PERMISSIONS = {
    'admin': ['read', 'write', 'delete'],
    'user': ['read', 'write'],
    'guest': ['read']
}

def authorize_user(role_required):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            auth_header = request.headers.get('Authorization')
            if not auth_header or not verify_token(auth_header, role_required):
                return jsonify({"error": "Unauthorized"}), 403
            return f(*args, **kwargs)
        return decorated_function
    return decorator

def verify_token(token, role_required):
    # Implement token verification logic and role check
    user_role = 'user'  # Placeholder: Extract role from token
    if user_role not in ROLE_PERMISSIONS:
        return False
    return role_required in ROLE_PERMISSIONS[user_role]