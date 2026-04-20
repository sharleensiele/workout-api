from server.app import app
from server.models import db, Exercise, Workout, WorkoutExercise
from datetime import date

with app.app_context():

    print("Clearing old data...")

    WorkoutExercise.query.delete()
    Exercise.query.delete()
    Workout.query.delete()

    db.session.commit()

    print("Creating exercises...")

    e1 = Exercise(name="Push Ups", category="Strength", equipment_needed=False)
    e2 = Exercise(name="Squats", category="Strength", equipment_needed=False)
    e3 = Exercise(name="Plank", category="Core", equipment_needed=False)

    db.session.add_all([e1, e2, e3])
    db.session.commit()

    print("Creating workout...")

    w1 = Workout(date=date.today(), duration_minutes=30, notes="Morning session")

    db.session.add(w1)
    db.session.commit()

    print("Linking exercises...")

    we1 = WorkoutExercise(workout_id=w1.id, exercise_id=e1.id, reps=15, sets=3)
    we2 = WorkoutExercise(workout_id=w1.id, exercise_id=e2.id, reps=20, sets=4)
    we3 = WorkoutExercise(workout_id=w1.id, exercise_id=e3.id, duration_seconds=60)

    db.session.add_all([we1, we2, we3])
    db.session.commit()

    print("Seeding complete 🎉")