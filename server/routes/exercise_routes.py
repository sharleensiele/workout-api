from flask import Blueprint, jsonify, request
from server.models import db, Exercise

exercise_bp = Blueprint("exercises", __name__)

# -----------------------------
# GET ALL EXERCISES
# -----------------------------
@exercise_bp.route("/", methods=["GET"])
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


# -----------------------------
# GET ONE EXERCISE
# -----------------------------
@exercise_bp.route("/<int:id>", methods=["GET"])
def get_exercise(id):
    exercise = Exercise.query.get(id)

    if not exercise:
        return jsonify({"error": "Exercise not found"}), 404

    return jsonify({
        "id": exercise.id,
        "name": exercise.name,
        "category": exercise.category,
        "equipment_needed": exercise.equipment_needed
    }), 200


# -----------------------------
# CREATE EXERCISE
# -----------------------------
@exercise_bp.route("/", methods=["POST"])
def create_exercise():
    data = request.get_json()

    exercise = Exercise(
        name=data["name"],
        category=data["category"],
        equipment_needed=data.get("equipment_needed", False)
    )

    db.session.add(exercise)
    db.session.commit()

    return jsonify({
        "message": "Exercise created",
        "id": exercise.id
    }), 201


# -----------------------------
# UPDATE EXERCISE (PATCH)
# -----------------------------
@exercise_bp.route("/<int:id>", methods=["PATCH"])
def update_exercise(id):
    exercise = Exercise.query.get(id)

    if not exercise:
        return jsonify({"error": "Exercise not found"}), 404

    data = request.get_json()

    if "name" in data:
        exercise.name = data["name"]

    if "category" in data:
        exercise.category = data["category"]

    if "equipment_needed" in data:
        exercise.equipment_needed = data["equipment_needed"]

    db.session.commit()

    return jsonify({"message": "Exercise updated"}), 200


# -----------------------------
# DELETE EXERCISE
# -----------------------------
@exercise_bp.route("/<int:id>", methods=["DELETE"])
def delete_exercise(id):
    exercise = Exercise.query.get(id)

    if not exercise:
        return jsonify({"error": "Exercise not found"}), 404

    db.session.delete(exercise)
    db.session.commit()

    return jsonify({"message": "Exercise deleted"}), 200