from flask import Blueprint, jsonify, request
from server.models.episode import Episode
from server.extensions import db
from flask_jwt_extended import jwt_required

episode_bp = Blueprint('episode_bp', __name__)

@episode_bp.route('/', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([{'id': e.id, 'date': e.date, 'number': e.number} for e in episodes])

@episode_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    episode = Episode.query.get(id)
    if episode:
        db.session.delete(episode)
        db.session.commit()
        return jsonify({'message': 'Episode deleted'})
    return jsonify({'error': 'Episode not found'}), 404
