from marshmallow import Schema, fields, validates, ValidationError

class WorkoutExerciseSchema(Schema):
    id = fields.Int(dump_only=True)

    workout_id = fields.Int(required=True)
    exercise_id = fields.Int(required=True)

    reps = fields.Int(allow_none=True)
    sets = fields.Int(allow_none=True)
    duration_seconds = fields.Int(allow_none=True)

    # ✅ Schema validation (3)
    @validates("reps")
    def validate_reps(self, value):
        if value is not None and value < 0:
            raise ValidationError("Reps cannot be negative")

    @validates("sets")
    def validate_sets(self, value):
        if value is not None and value < 0:
            raise ValidationError("Sets cannot be negative")

    @validates("duration_seconds")
    def validate_duration(self, value):
        if value is not None and value < 0:
            raise ValidationError("Duration cannot be negative")