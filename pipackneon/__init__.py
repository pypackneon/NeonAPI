"""
PyPackNeon Flask App Factory 🐍
Creates and configures the Flask app with all routes and database setup.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

# Initialize database object globally for models
db = SQLAlchemy()

def create_app():
    """Create and configure the Flask app"""
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize database with app context
    db.init_app(app)

    # Import and register routes
    from .routes import api
    app.register_blueprint(api, url_prefix='/api')

    return app
