from server.app import db, ma


class CompetitionTeamPlayer(db.Model):
    __tablename__ = 'competition_team_player'

    id = db.Column(db.Integer, primary_key=True)
    competition_team_id = db.Column(db.Integer, db.ForeignKey('competition_team.id'), nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)
    position_id = db.Column(db.Integer, db.ForeignKey('position.id'), nullable=False)
    captain = db.Column(db.Boolean, nullable=False)

    def __init__(self, competition_team_id, player_id, captain):
        self.competition_team_id = competition_team_id
        self.player_id = player_id
        self.points = captain

    def __repr__(self):
        return f"{self.id}"


class CompetitionTeamPlayerSchema(ma.SQLAlchemySchema):
    class Meta:
        model = CompetitionTeamPlayer

    id = ma.auto_field()
    competition_team_id = ma.auto_field()
    player_id = ma.auto_field()
    points = ma.auto_field()


competition_team_player_schema = CompetitionTeamPlayerSchema()
competition_teams_player_schema = CompetitionTeamPlayerSchema(many=True)