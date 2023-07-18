from server.app import db, ma


class SportTypePositionType(db.Model):
    __tablename__ = 'sport_type_position_type'

    id = db.Column(db.Integer, primary_key=True)
    sport_type_id = db.Column(db.Integer, db.ForeignKey('sport_type.id'), required=True)
    position_type_id = db.Column(db.Integer, db.ForeignKey('position_type.id'), required=True)
    number = db.Column(db.Integer, required=True)

    def __init__(self, name, active):
        self.name = name
        self.active = active

    def __repr__(self):
        return f"{self.id}"


class SportTypeSchema(ma.SQLAlchemySchema):
    class Meta:
        model = SportTypePositionType

    id = ma.auto_field()
    name = ma.auto_field()
    active = ma.auto_field()


sport_type_schema = SportTypeSchema()
sport_types_schema = SportTypeSchema(many=True)