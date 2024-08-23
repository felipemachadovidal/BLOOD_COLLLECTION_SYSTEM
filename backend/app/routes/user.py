from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models.user import User
from ..schemas.user import UserSchema

user_bp = Blueprint('user_bp', __name__)
user_schema = UserSchema()

@user_bp.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    user_id = get_jwt_identity()
    user = User.query.get_or_404(user_id)
    return user_schema.jsonify(user)
