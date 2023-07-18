from server.app import db, ma


class SkillType(db.Model):
    __tablename__ = 'skill_type'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), required=True)
    active = db.Column(db.Boolean, required=True)

    def __init__(self, name, active):
        self.name = name
        self.active = active

    def __repr__(self):
        return f"{self.id}"


class SkillTypeSchema(ma.SQLAlchemySchema):
    class Meta:
        model = SkillType

    id = ma.auto_field()
    name = ma.auto_field()
    active = ma.auto_field()


skill_type_schema = SkillTypeSchema()
skill_types_schema = SkillTypeSchema(many=True)