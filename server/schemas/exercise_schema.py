from marshmallow import Schema, fields, validates, ValidationError

class ExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    category = fields.Str(required=True)
    equipment_needed = fields.Bool(required=True)

    # ✅ Schema validation (1)
    @validates("name")
    def validate_name(self, value):
        if len(value) < 2:
            raise ValidationError("Exercise name must be at least 2 characters long")