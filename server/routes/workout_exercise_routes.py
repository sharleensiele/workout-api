from flask import Blueprint, jsonify, request
from server.models import db
from server.models.workout_exercise import WorkoutExercise
from server.models.workout import Workout
from server.models.exercise import Exercise

workout_exercise_bp = Blueprint("workout_exercise_bp", __name__)

# -------------------------------------------------
# ADD EXERCISE TO WORKOUT (CREATE LINK)
# -------------------------------------------------
@workout_exercise_bp.route("/", methods=["POST"])
def add_exercise_to_workout():

    data = request.get_json()

    workout_id = data.get("workout_id")
    exercise_id = data.get("exercise_id")

    workout = Workout.query.get(workout_id)
    exercise = Exercise.query.get(exercise_id)

    if not workout:
        return jsonify({"error": "Workout not found"}), 404

    if not exercise:
        return jsonify({"error": "Exercise not found"}), 404

    try:
        workout_exercise = WorkoutExercise(
            workout_id=workout_id,
            exercise_id=exercise_id,
            reps=data.get("reps"),
            sets=data.get("sets"),
            duration_seconds=data.get("duration_seconds")
        )

        db.session.add(workout_exercise)
        db.session.commit()

        return jsonify({
            "message": "Exercise added to workout",
            "workout_exercise": {
                "id": workout_exercise.id,
                "workout_id": workout_exercise.workout_id,
                "exercise_id": workout_exercise.exercise_id,
                "reps": workout_exercise.reps,
                "sets": workout_exercise.sets,
                "duration_seconds": workout_exercise.duration_seconds
            }
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400


# -------------------------------------------------
# GET ALL WORKOUT EXERCISES
# -------------------------------------------------
@workout_exercise_bp.route("/", methods=["GET"])
def get_workout_exercises():

    links = WorkoutExercise.query.all()

    return jsonify([
        {
            "id": link.id,
            "workout_id": link.workout_id,
            "exercise_id": link.exercise_id,
            "reps": link.reps,
            "sets": link.sets,
            "duration_seconds": link.duration_seconds
        }
        for link in links
    ]), 200


# -------------------------------------------------
# DELETE WORKOUT EXERCISE LINK
# -------------------------------------------------
@workout_exercise_bp.route("/<int:id>", methods=["DELETE"])
def delete_workout_exercise(id):

    link = WorkoutExercise.query.get(id)

    if not link:
        return jsonify({"error": "WorkoutExercise not found"}), 404

    db.session.delete(link)
    db.session.commit()

    return jsonify({"message": "Deleted successfully"}), 200