from server.app import db, ma


class SportType(db.Model):
    __tablename__ = 'sport_type'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), required=True)
    active = db.Column(db.Boolean, required=True)

    def __init__(self, name, active):
        self.name = name
        self.active = active

    def __repr__(self):
        return f"{self.id}"


class SportTypeSchema(ma.SQLAlchemySchema):
    class Meta:
        model = SportType

    id = ma.auto_field()
    name = ma.auto_field()
    active = ma.auto_field()


sport_type_schema = SportTypeSchema()
sport_types_schema = SportTypeSchema(many=True)