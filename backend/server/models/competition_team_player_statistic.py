from server.app import db, ma


class CompetitionTeamPlayerStatistic(db.Model):
    __tablename__ = 'competition_team_player_statistic'

    id = db.Column(db.Integer, primary_key=True)
    competition_team_player_id = db.Column(db.Integer, db.ForeignKey('competition_team_player.id'), required=True)
    statistic_id = db.Column(db.Integer, db.ForeignKey('statistic.id'), required=True)
    value = db.Column(db.Integer, db.ForeignKey('position.id'), required=True)

    def __init__(self, competition_team_player_id, statistic_id, value):
        self.competition_team_player_id = competition_team_player_id
        self.statistic_id = statistic_id
        self.value = value

    def __repr__(self):
        return f"{self.id}"


class CompetitionTeamPlayerStatisticSchema(ma.SQLAlchemySchema):
    class Meta:
        model = CompetitionTeamPlayerStatistic

    id = ma.auto_field()
    competition_team_player_id = ma.auto_field()
    player_id = ma.auto_field()
    value = ma.auto_field()


competition_team_player_statistic_schema = CompetitionTeamPlayerStatisticSchema()
competition_teams_player_statistic_schema = CompetitionTeamPlayerStatisticSchema(many=True)