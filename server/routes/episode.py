from flask import Blueprint, jsonify, request
from server.models.episode import Episode
from server.extensions import db

episode_bp = Blueprint('episode_bp', __name__)

@episode_bp.route('/episodes/', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([{"id": e.id, "title": e.title} for e in episodes]), 200

@episode_bp.route('/episodes/<int:id>', methods=['DELETE'])
def delete_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify(message="Episode not found."), 404
    db.session.delete(episode)
    db.session.commit()
    return jsonify(message="Episode deleted."), 200

