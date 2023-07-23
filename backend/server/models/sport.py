from server.app import db, ma


class Sport(db.Model):
    __tablename__ = 'sport'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    active = db.Column(db.Boolean, nullable=False)

    def __init__(self, name, active):
        self.name = name
        self.active = active

    def __repr__(self):
        return f"{self.id}"


class SportSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Sport

    id = ma.auto_field()
    name = ma.auto_field()
    active = ma.auto_field()


sport_schema = SportSchema()
sports_schema = SportSchema(many=True)