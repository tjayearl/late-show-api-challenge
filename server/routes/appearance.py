from flask import Blueprint, request, jsonify
from server.models.appearance import Appearance
from server.extensions import db

appearance_bp = Blueprint('appearance_bp', __name__)

@appearance_bp.route('/appearances/', methods=['POST'])
def create_appearance():
    data = request.get_json()
    try:
        new_appearance = Appearance(
            rating=data['rating'],
            guest_id=data['guest_id'],
            episode_id=data['episode_id']
        )
        db.session.add(new_appearance)
        db.session.commit()
        return jsonify(message="Appearance created."), 201
    except Exception as e:
        return jsonify(message=str(e)), 400
