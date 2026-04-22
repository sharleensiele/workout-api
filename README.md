# 🚀 Workout API (Flask + SQLite)

A REST API built with Flask and SQLAlchemy for managing workouts, exercises, and their relationships.

---

## 📦 Features
- Flask REST API
- SQLAlchemy ORM
- SQLite database (`app.db`)
- CRUD for Exercises & Workouts
- Many-to-many relationship (Workout ↔ Exercises)
- Clean modular structure using Blueprints

---

## 🛠️ Tech Stack
Python 3.12+, Flask, Flask SQLAlchemy, SQLite

---

## 📁 Setup Instructions

### 1. Clone the project
git clone <your-repo-url>  
cd workout-api  

---

### 2. Install dependencies
pip install flask flask-sqlalchemy  

(or if using pipenv)
pipenv install  
pipenv shell  

---

### 3. Run the application
python -m server.app  

Server runs at:
http://127.0.0.1:5555  

---

## 📡 API Endpoints

### 🏋️ Exercises
GET /exercises/ → Get all exercises  
GET /exercises/<id> → Get single exercise  
POST /exercises/ → Create exercise  
PATCH /exercises/<id> → Update exercise  
DELETE /exercises/<id> → Delete exercise  

---

### 🏃 Workouts
GET /workouts/ → Get all workouts  
GET /workouts/<id> → Get single workout  
POST /workouts/ → Create workout  
PATCH /workouts/<id> → Update workout  
DELETE /workouts/<id> → Delete workout  

---

### 🔗 Workout Exercises (Join Table)
GET /workout-exercises/ → Get all workout links  
POST /workout-exercises/ → Add exercise to workout  
DELETE /workout-exercises/<id> → Remove link  

---

## 🧪 Example POST (Workout Exercise)

```json
{
  "workout_id": 1,
  "exercise_id": 2,
  "reps": 15,
  "sets": 3,
  "duration_seconds": null
}
Use Postman for testing endpoints

''DATABASE''
SQLite database file: server/instance/app.db
Tables auto-created using db.create_all()