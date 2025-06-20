from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from server.models.episode import Episode
from server.models.appearance import Appearance
from server.app import db

episode_bp = Blueprint('episodes', __name__, url_prefix='/episodes')

@episode_bp.route('/', methods=['GET'])
def list_episodes():
    episodes = Episode.query.all()
    return jsonify([{"id": ep.id, "date": ep.date.isoformat(), "number": ep.number} for ep in episodes])

@episode_bp.route('/<int:id>', methods=['GET'])
def get_episode(id):
    ep = Episode.query.get_or_404(id)
    return jsonify({
        "id": ep.id,
        "date": ep.date.isoformat(),
        "number": ep.number,
        "appearances": [{"id": a.id, "rating": a.rating} for a in ep.appearances]
    })

@episode_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    ep = Episode.query.get_or_404(id)
    db.session.delete(ep)
    db.session.commit()
    return jsonify(message="Episode deleted")
