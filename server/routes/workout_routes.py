from flask import Blueprint, jsonify, request
from server.models import db, Workout
from datetime import datetime

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
# GET ONE WORKOUT
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
        "notes": workout.notes
    }), 200


# -----------------------------
# CREATE WORKOUT (FIXED)
# -----------------------------
@workout_bp.route("/", methods=["POST"])
def create_workout():
    data = request.get_json()

    try:
        # ✅ FIX: convert string → Python date object
        workout_date = datetime.strptime(data["date"], "%Y-%m-%d").date()

        workout = Workout(
            date=workout_date,
            duration_minutes=data["duration_minutes"],
            notes=data.get("notes")
        )

        db.session.add(workout)
        db.session.commit()

        return jsonify({
            "message": "Workout created",
            "id": workout.id
        }), 201

    except KeyError as e:
        return jsonify({"error": f"Missing field: {str(e)}"}), 400

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


# -----------------------------
# UPDATE WORKOUT (PATCH FIXED)
# -----------------------------
@workout_bp.route("/<int:id>", methods=["PATCH"])
def update_workout(id):
    workout = Workout.query.get(id)

    if not workout:
        return jsonify({"error": "Workout not found"}), 404

    data = request.get_json()

    if "date" in data:
        workout.date = datetime.strptime(data["date"], "%Y-%m-%d").date()

    if "duration_minutes" in data:
        workout.duration_minutes = data["duration_minutes"]

    if "notes" in data:
        workout.notes = data["notes"]

    db.session.commit()

    return jsonify({"message": "Workout updated"}), 200


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