from flask import Blueprint, jsonify

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/')
def home():
    return jsonify(message="Welcome to the Late Show API!"), 200