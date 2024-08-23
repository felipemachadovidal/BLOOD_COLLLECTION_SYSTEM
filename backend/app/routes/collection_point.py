from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models.collection_point import CollectionPoint
from .. import db
from ..schemas.collection_point import CollectionPointSchema

collection_point_bp = Blueprint('collection_point_bp', __name__)
collection_point_schema = CollectionPointSchema()
collection_points_schema = CollectionPointSchema(many=True)

@collection_point_bp.route('/', methods=['POST'])
@jwt_required()
def create_collection_point():
    data = request.get_json()
    user_id = get_jwt_identity()
    collection_point = CollectionPoint(
        name=data.get('name'),
        address=data.get('address'),
        user_id=user_id
    )
    db.session.add(collection_point)
    db.session.commit()
    return collection_point_schema.jsonify(collection_point), 201

@collection_point_bp.route('/', methods=['GET'])
@jwt_required()
def get_collection_points():
    user_id = get_jwt_identity()
    collection_points = CollectionPoint.query.filter_by(user_id=user_id).all()
    return collection_points_schema.jsonify(collection_points)
