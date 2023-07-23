from server.app import db, ma


class Competition(db.Model):
    __tablename__ = 'competition'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    sport_id = db.Column(db.Integer, db.ForeignKey('sport.id'), nullable=False)
    structure_id = db.Column(db.Integer, db.ForeignKey('structure.id'), nullable=False)
    image = db.Column(db.String(80), nullable=False)

    win_points = db.Column(db.Integer, primary_key=True)
    bye_points = db.Column(db.Integer, primary_key=True)
    draw_points = db.Column(db.Integer, primary_key=True)

    def __init__(self, name, sport_id, structure_id, image, win_points, bye_points, draw_points):
        self.name = name
        self.sport_id = sport_id
        self.structure_id = structure_id
        self.image = image

        self.win_points = win_points
        self.bye_points = bye_points
        self.draw_points = draw_points

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
    win_points = ma.auto_field()
    bye_points = ma.auto_field()
    draw_points = ma.auto_field()


competition_schema = CompetitionSchema()
competitions_schema = CompetitionSchema(many=True)