from flask import Blueprint, jsonify, request
from server.models import db, Workout

workout_bp = Blueprint("workouts", __name__)

# -----------------------------
# GET ALL WORKOUTS
# -----------------------------
@workout_bp.route("/", methods=["GET"])
def get_workouts():
    workouts = Workout.query.all()

    return jsonify([
        {
            "id": w.id,
            "date": str(w.date),
            "duration_minutes": w.duration_minutes,
            "notes": w.notes
        }
        for w in workouts
    ]), 200


# -----------------------------
# GET SINGLE WORKOUT
# -----------------------------
@workout_bp.route("/<int:id>", methods=["GET"])
def get_workout(id):
    workout = Workout.query.get(id)

    if not workout:
        return jsonify({"error": "Workout not found"}), 404

    return jsonify({
        "id": workout.id,
        "date": str(workout.date),
        "duration_minutes": workout.duration_minutes,
        "notes": workout.notes,
        "exercises": [
            {
                "id": we.exercise.id,
                "name": we.exercise.name,
                "category": we.exercise.category,
                "equipment_needed": we.exercise.equipment_needed,
                "reps": we.reps,
                "sets": we.sets,
                "duration_seconds": we.duration_seconds
            }
            for we in workout.workout_exercises
        ]
    }), 200


# -----------------------------
# CREATE WORKOUT
# -----------------------------
@workout_bp.route("/", methods=["POST"])
def create_workout():
    data = request.get_json()

    try:
        workout = Workout(
            date=data["date"],
            duration_minutes=data["duration_minutes"],
            notes=data.get("notes")
        )

        db.session.add(workout)
        db.session.commit()

        return jsonify({
            "message": "Workout created",
            "id": workout.id
        }), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 400


# -----------------------------
# DELETE WORKOUT
# -----------------------------
@workout_bp.route("/<int:id>", methods=["DELETE"])
def delete_workout(id):
    workout = Workout.query.get(id)

    if not workout:
        return jsonify({"error": "Workout not found"}), 404

    db.session.delete(workout)
    db.session.commit()

    return jsonify({"message": "Workout deleted"}), 200