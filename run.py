"""
Run PyPackNeon API 🐍
Entry point for the development server.
"""

from pypackneon import create_app, db
from pypackneon.pipackneon.models import User, Post

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run()
