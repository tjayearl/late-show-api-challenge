from flask import Blueprint, request, jsonify
from server.models.appearance import Appearance
from server.extensions import db
from flask_jwt_extended import jwt_required

appearance_bp = Blueprint('appearance_bp', __name__)

@appearance_bp.route('/', methods=['POST'])
@jwt_required()
def create_appearance():
    data = request.get_json()
    appearance = Appearance(rating=data['rating'], guest_id=data['guest_id'], episode_id=data['episode_id'])
    db.session.add(appearance)
    db.session.commit()
    return jsonify({'message': 'Appearance created'})