# 🐍 NeonAPI - Flask Skeleton

Welcome to NeonAPI! This project is a ready-to-use skeleton for building REST APIs with Flask, already set up for database integration using SQLAlchemy.

---

## 🐍 Repository
Official repository: [https://github.com/pypackneon/NeonAPI.git](https://github.com/pypackneon/NeonAPI.git)

---

## 🐍 Quick Start Guide

### 1. Clone the repository
```sh
git clone https://github.com/pypackneon/NeonAPI.git
cd NeonAPI
```

### 2. Create and activate a virtual environment
```powershell
python -m venv .venv
.venv\Scripts\Activate
```

### 3. Install dependencies
```sh
pip install -r pypackneon/requirements.txt
```

### 4. Configure your database
Edit `pypackneon/pipackneon/config.py` and set your database URI:
```python
SQLALCHEMY_DATABASE_URI = 'sqlite:///mydb.db'  # Or use PostgreSQL/MySQL
```

### 5. Run the application
```sh
python -m pypackneon.run
```
Your API will be available at: `http://127.0.0.1:5000/api/`

---

## 🐍 Project Structure
```
pypackneon/
  pipackneon/
    config.py      # 🐍 Project settings
    models.py      # 🐍 Database models
    routes.py      # 🐍 API endpoints
    __init__.py    # 🐍 App factory
  tests/           # 🐍 Automated tests
  run.py           # 🐍 Entry point
README.md
requirements.txt
```

---

## 🐍 Running Tests
To run automated tests:
```sh
pytest pypackneon/tests/
```

---

## 🐍 Connecting to Your Database
- Edit `config.py` and set the URI for your preferred database.
- Create your models in `models.py`.
- Use `db.session` in your routes to interact with the database.

### Example database URIs
- SQLite: `sqlite:///mydb.db`
- PostgreSQL: `postgresql://user:password@localhost:5432/mydb`
- MySQL: `mysql+pymysql://user:password@localhost:3306/mydb`

---

## 🐍 Example: Creating a Model
In `models.py`:
```python
from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
```

---

## 🐍 Example: Using Your Model in a Route
In `routes.py`:
```python
from .models import User, db

@api.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(username=data['username'], email=data['email'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'id': user.id, 'username': user.username}), 201
```

---

## 🐍 Tips
- All configuration is in `config.py`.
- All models go in `models.py`.
- All API endpoints go in `routes.py`.
- Use the test folder to keep your automated tests organized.

---

If you need more examples or want to expand your API, check the project files or ask for help! 🐍
