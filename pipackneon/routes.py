"""
PyPackNeon API Routes 🐍
Skeleton REST endpoints for CRUD operations.
Adapt the logic to your project data or database.
"""

from flask import Blueprint, jsonify, request
from .models import db, User, Post

# Blueprint registration
api = Blueprint('api', __name__)

# Health check endpoint
@api.route('/health', methods=['GET'])
def health_check():
    """Check if API is running"""
    return jsonify(status="healthy"), 200

# GET all items (example: users)
@api.route('/users', methods=['GET'])
def get_users():
    """Return all users"""
    users = User.query.all()
    return jsonify([{'id': u.id, 'username': u.username, 'email': u.email} for u in users]), 200

# POST create a new user
@api.route('/users', methods=['POST'])
def create_user():
    """Create a new user"""
    data = request.get_json()
    user = User(username=data['username'], email=data['email'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'id': user.id, 'username': user.username, 'email': user.email}), 201

# GET single user by ID
@api.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Return a single user by ID"""
    user = User.query.get_or_404(user_id)
    return jsonify({'id': user.id, 'username': user.username, 'email': user.email}), 200

# PUT update user by ID
@api.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Update an existing user"""
    user = User.query.get_or_404(user_id)
    data = request.get_json()
    user.username = data.get('username', user.username)
    user.email = data.get('email', user.email)
    db.session.commit()
    return jsonify({'id': user.id, 'username': user.username, 'email': user.email}), 200

# DELETE user by ID
@api.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Delete a user"""
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify(message="User deleted"), 204
