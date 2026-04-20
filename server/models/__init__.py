from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .exercise import Exercise
from .workout import Workout
from .workout_exercise import WorkoutExercise