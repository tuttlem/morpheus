from server.app import db, ma


class PlayerSkill(db.Model):
    __tablename__ = 'player_skill'

    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), required=True)
    skill_id = db.Column(db.Integer, db.ForeignKey('skill.id'), required=True)
    level = db.Column(db.Integer, required=True)

    def __init__(self, player_id, skill_id, level):
        self.player_id = player_id
        self.skill_id = skill_id
        self.level = level

    def __repr__(self):
        return f"{self.id}"


class PlayerSkillSchema(ma.SQLAlchemySchema):
    class Meta:
        model = PlayerSkill

    id = ma.auto_field()
    player_id = ma.auto_field()
    skill_id = ma.auto_field()
    level = ma.auto_field()


sport_type_schema = PlayerSkillSchema()
sport_types_schema = PlayerSkillSchema(many=True)