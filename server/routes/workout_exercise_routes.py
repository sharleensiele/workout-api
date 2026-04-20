from flask import Blueprint, request, jsonify
from server.models import db, WorkoutExercise, Workout, Exercise

workout_exercise_bp = Blueprint("workout_exercise_bp", __name__)

# -------------------------------------------------
# ADD EXERCISE TO WORKOUT (JOIN TABLE CREATE)
# -------------------------------------------------
@workout_exercise_bp.route(
    "/workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises",
    methods=["POST"]
)
def add_exercise_to_workout(workout_id, exercise_id):

    workout = Workout.query.get(workout_id)
    exercise = Exercise.query.get(exercise_id)

    # ✅ Validate existence
    if not workout:
        return jsonify({"error": "Workout not found"}), 404

    if not exercise:
        return jsonify({"error": "Exercise not found"}), 404

    data = request.get_json()

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
            "message": "Exercise successfully added to workout",
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
# (OPTIONAL BUT GOOD) GET ALL WORKOUT EXERCISES
# -------------------------------------------------
@workout_exercise_bp.route("/workout_exercises", methods=["GET"])
def get_workout_exercises():

    all_links = WorkoutExercise.query.all()

    return jsonify([
        {
            "id": we.id,
            "workout_id": we.workout_id,
            "exercise_id": we.exercise_id,
            "reps": we.reps,
            "sets": we.sets,
            "duration_seconds": we.duration_seconds
        }
        for we in all_links
    ]), 200


# -------------------------------------------------
# (OPTIONAL) DELETE LINK
# -------------------------------------------------
@workout_exercise_bp.route("/workout_exercises/<int:id>", methods=["DELETE"])
def delete_workout_exercise(id):

    we = WorkoutExercise.query.get(id)

    if not we:
        return jsonify({"error": "WorkoutExercise not found"}), 404

    db.session.delete(we)
    db.session.commit()

    return jsonify({"message": "Deleted successfully"}), 200