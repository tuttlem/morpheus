from server.app import db, ma


class SportPosition(db.Model):
    __tablename__ = 'sport_position'

    id = db.Column(db.Integer, primary_key=True)
    sport_id = db.Column(db.Integer, db.ForeignKey('sport.id'), nullable=False)
    position_id = db.Column(db.Integer, db.ForeignKey('position.id'), nullable=False)
    number = db.Column(db.Integer, nullable=False)

    def __init__(self, sport_id, position_id, number):
        self.sport_id = sport_id
        self.position_id = position_id
        self.number = number

    def __repr__(self):
        return f"{self.id}"


class SportPositionSchema(ma.SQLAlchemySchema):
    class Meta:
        model = SportPosition

    id = ma.auto_field()
    sport_id = ma.auto_field()
    position_id = ma.auto_field()
    numer = ma.auto_field()


sport_type_schema = SportPositionSchema()
sport_types_schema = SportPositionSchema(many=True)