from server.app import db, ma


class CompetitionTeam(db.Model):
    __tablename__ = 'competition_team'

    id = db.Column(db.Integer, primary_key=True)
    competition_id = db.Column(db.Integer, db.ForeignKey('competition.id'), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    points = db.Column(db.Integer, nullable=False)

    def __init__(self, competition_id, team_id, points):
        self.competition_id = competition_id
        self.team_id = team_id
        self.points = points

    def __repr__(self):
        return f"{self.id}"


class CompetitionTeamSchema(ma.SQLAlchemySchema):
    class Meta:
        model = CompetitionTeam

    id = ma.auto_field()
    competition_id = ma.auto_field()
    team_id = ma.auto_field()
    points = ma.auto_field()


competition_team_schema = CompetitionTeamSchema()
competition_teams_schema = CompetitionTeamSchema(many=True)