from flask import Flask
from flask_migrate import Migrate

from server.models import db
from server.routes.workout_routes import workout_bp
from server.routes.exercise_routes import exercise_bp
from server.routes.workout_exercise_routes import workout_exercise_bp

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    Migrate(app, db)

    # REGISTER BLUEPRINTS (NO PREFIX MISTAKES HERE)
    app.register_blueprint(workout_bp, url_prefix="/workouts")
    app.register_blueprint(exercise_bp, url_prefix="/exercises")
    app.register_blueprint(workout_exercise_bp)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(port=5555, debug=True)