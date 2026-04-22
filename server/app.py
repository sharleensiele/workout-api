import os
from flask import Flask
from flask_migrate import Migrate

from server.models import db
from server.routes.workout_routes import workout_bp
from server.routes.exercise_routes import exercise_bp
from server.routes.workout_exercise_routes import workout_exercise_bp


def create_app():
    app = Flask(__name__)

    # ---------------------------------
    # DATABASE CONFIG 
    # ---------------------------------
    base_dir = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(base_dir, "instance", "app.db")

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + db_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Ensure instance folder exists
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    # ---------------------------------
    # INIT EXTENSIONS
    # ---------------------------------
    db.init_app(app)
    migrate = Migrate(app, db)

    # ---------------------------------
    # REGISTER BLUEPRINTS
    # ---------------------------------
    app.register_blueprint(workout_bp, url_prefix="/workouts")
    app.register_blueprint(exercise_bp, url_prefix="/exercises")
    app.register_blueprint(workout_exercise_bp, url_prefix="/workout-exercises")

    # ---------------------------------
    # HOME ROUTE (for testing)
    # ---------------------------------
    @app.route("/")
    def home():
        return {"message": "Workout API is running 🚀"}, 200

    # ---------------------------------
    # CREATE TABLES (SAFE INIT)
    # ---------------------------------
    with app.app_context():
        db.create_all()

    return app


app = create_app()

if __name__ == "__main__":
    app.run(port=5555, debug=True)