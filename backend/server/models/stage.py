from server.app import db, ma


class Stage(db.Model):
    __tablename__ = 'stage'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    active = db.Column(db.Boolean, nullable=False)

    def __init__(self, name, active):
        self.name = name
        self.active = active

    def __repr__(self):
        return f"{self.id}"


class StageSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Stage

    id = ma.auto_field()
    name = ma.auto_field()
    active = ma.auto_field()


stage_schema = StageSchema()
stages_schema = StageSchema(many=True)