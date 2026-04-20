from . import db
from sqlalchemy.orm import validates

class Exercise(db.Model):
    __tablename__ = "exercises"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    equipment_needed = db.Column(db.Boolean, default=False)

    workout_exercises = db.relationship(
        "WorkoutExercise",
        back_populates="exercise",
        cascade="all, delete-orphan"
    )

    @validates("name")
    def validate_name(self, key, value):
        if not value or len(value) < 2:
            raise ValueError("Name must be at least 2 characters")
        return value

    @validates("category")
    def validate_category(self, key, value):
        if not value:
            raise ValueError("Category cannot be empty")
        return value