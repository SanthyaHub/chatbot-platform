from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from flask_cors import CORS
import sqlite3
import hashlib
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-change-this'  # Change for security
app.config['JWT_SECRET_KEY'] = 'your-jwt-secret-key-change-this'  # Change for security
jwt = JWTManager(app)
CORS(app)

# Database Setup
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY, email TEXT UNIQUE, password TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS projects
                 (id INTEGER PRIMARY KEY, user_id INTEGER, name TEXT, prompts TEXT)''')
    conn.commit()
    conn.close()

init_db()

# Password Hashing
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Routes
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    email = data['email']
    password = hash_password(data['password'])
    try:
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
        conn.commit()
        conn.close()
        return jsonify({'message': 'User  registered!'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'error': 'Email already exists'}), 400

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data['email']
    password = hash_password(data['password'])
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT id FROM users WHERE email=? AND password=?", (email, password))
    user = c.fetchone()
    conn.close()
    if user:
        access_token = create_access_token(identity=str(user[0]))  # String for JWT
        return jsonify({'access_token': access_token})
    return jsonify({'error': 'Invalid credentials'}), 401

@app.route('/projects', methods=['POST'])
@jwt_required()
def create_project():
    user_id = int(get_jwt_identity())  # Convert back to int
    data = request.json
    name = data['name']
    prompts = data.get('prompts', '')
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT INTO projects (user_id, name, prompts) VALUES (?, ?, ?)", (user_id, name, prompts))
    conn.commit()
    project_id = c.lastrowid
    conn.close()
    return jsonify({'project_id': project_id, 'message': 'Project created!'}), 201

@app.route('/chat/<int:project_id>', methods=['POST'])
@jwt_required()
def chat(project_id):
    user_id = int(get_jwt_identity())  # Convert back to int
    data = request.json
    message = data['message']
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT prompts FROM projects WHERE id=? AND user_id=?", (project_id, user_id))
    result = c.fetchone()
    conn.close()
    if not result:
        return jsonify({'error': 'Project not found'}), 404
    prompts = result[0]
    
    # Simple Mock AI Response (No Real API - For Assignment Demo)
    ai_reply = f"Mock AI Reply: Based on your project prompts '{prompts}', responding to '{message}': This is a simulated chatbot response. In a real app, this would call OpenAI!"
    return jsonify({'reply': ai_reply})

if __name__ == '__main__':
    app.run(debug=True)
