from server.app import db, ma


class Team(db.Model):
    __tablename__ = 'team'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), required=True)
    home_stadium_id = db.Column(db.Integer, db.ForeignKey('stadium.id'), required=True)
    image = db.Column(db.String(80), required=True)

    def __init__(self, name, home_stadium_id, image):
        self.name = name
        self.home_stadium_id = home_stadium_id
        self.image = image

    def __repr__(self):
        return f"{self.id}"


class TeamSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Team

    id = ma.auto_field()
    name = ma.auto_field()
    home_stadium_id = ma.auto_field()
    image = ma.auto_field()


team_schema = TeamSchema()
teams_schema = TeamSchema(many=True)