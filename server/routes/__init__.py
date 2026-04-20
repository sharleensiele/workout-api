# This file makes "routes" a Python package.

from .exercise_routes import exercise_bp
from .workout_routes import workout_bp
from .workout_exercise_routes import workout_exercise_bp

__all__ = [
    "exercise_bp",
    "workout_bp",
    "workout_exercise_bp"
]