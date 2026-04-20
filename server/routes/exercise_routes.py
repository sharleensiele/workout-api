from flask import Blueprint, jsonify
from server.models import Exercise

exercise_bp = Blueprint("exercise_bp", __name__)

@exercise_bp.route("/exercises", methods=["GET"])
def get_exercises():
    exercises = Exercise.query.all()

    return jsonify([
        {
            "id": e.id,
            "name": e.name,
            "category": e.category,
            "equipment_needed": e.equipment_needed
        }
        for e in exercises
    ]), 200