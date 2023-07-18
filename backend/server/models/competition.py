from server.app import db, ma


class Competition(db.Model):
    __tablename__ = 'competition'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), required=True)
    sport_id = db.Column(db.Integer, db.ForeignKey('sport.id'), required=True)
    structure_id = db.Column(db.Integer, db.ForeignKey('structure.id'), required=True)
    image = db.Column(db.String(80), required=True)

    def __init__(self, name, sport_id, structure_id, image):
        self.name = name
        self.sport_id = sport_id
        self.structure_id = structure_id
        self.image = image

    def __repr__(self):
        return f"{self.id}"


class CompetitionSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Competition

    id = ma.auto_field()
    name = ma.auto_field()
    sport_id = ma.auto_field()
    structure_id = ma.auto_field()
    image = ma.auto_field()


competition_schema = CompetitionSchema()
competitions_schema = CompetitionSchema(many=True)