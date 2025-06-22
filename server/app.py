from flask import Flask
from flask_cors import CORS

from server.extensions import db, migrate, jwt

from server.routes.auth import auth_bp
from server.routes.guest import guest_bp
from server.routes.episode import episode_bp
from server.routes.appearance import appearance_bp
from server.routes.main import main_bp  # This is the new route for '/'

def create_app():
    app = Flask(__name__)

    # Load configuration from .env or directly set here
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this in production!

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    CORS(app)

    # Register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(guest_bp)
    app.register_blueprint(episode_bp)
    app.register_blueprint(appearance_bp)

    return app


# Required for `flask run`
app = create_app()
