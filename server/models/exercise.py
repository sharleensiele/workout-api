from sqlalchemy.orm import validates
from server.models import db

class Exercise(db.Model):
    __tablename__ = "exercises"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    equipment_needed = db.Column(db.Boolean, nullable=False)

    workout_exercises = db.relationship("WorkoutExercise", back_populates="exercise", cascade="all, delete")

    # Model validation
    @validates("name")
    def validate_name(self, key, value):
        if not value or len(value) < 2:
            raise ValueError("Exercise name must be at least 2 characters")
        return value