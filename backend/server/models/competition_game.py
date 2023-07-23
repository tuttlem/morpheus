from server.app import db, ma


class CompetitionGame(db.Model):
    __tablename__ = 'competition_game'

    id = db.Column(db.Integer, primary_key=True)

    competition_id = db.Column(db.Integer, db.ForeignKey('competition.id'), nullable=False)
    round = db.Column(db.Integer, nullable=False)
    game_number = db.Column(db.Integer, nullable=False)
    stage_id = db.Column(db.Integer, db.ForeignKey('stage.id'), nullable=False)

    home_team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    home_score = db.Column(db.Integer)

    away_team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    away_score = db.Column(db.Integer)

    stadium_id = db.Column(db.Integer, db.ForeignKey('stadium.id'), nullable=False)

    def __init__(self, competition_id, round_num, game_number, stage_id, home_team_id, home_score, away_team_id, away_score, stadium_id):
        self.competition_id = competition_id
        self.round = round_num
        self.game_number = game_number
        self.stage_id = stage_id
        self.home_team_id = home_team_id
        self.home_score = home_score
        self.away_team_id = away_team_id
        self.away_score = away_score
        self.stadium_id = stadium_id

    def __repr__(self):
        return f"{self.id}"


class CompetitionGameSchema(ma.SQLAlchemySchema):
    class Meta:
        model = CompetitionGame

    id = ma.auto_field()
    competition_id = ma.auto_field()
    round = ma.auto_field()
    game_number = ma.auto_field()
    stage_id = ma.auto_field()
    home_team_id = ma.auto_field()
    home_score = ma.auto_field()
    away_team_id = ma.auto_field()
    away_score = ma.auto_field()
    stadium_id = ma.auto_field()


competition_game_schema = CompetitionGameSchema()
competition_games_schema = CompetitionGameSchema(many=True)