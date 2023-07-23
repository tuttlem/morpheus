from server.app import db, ma


class Statistic(db.Model):
    __tablename__ = 'statistic'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    active = db.Column(db.Boolean, nullable=False)

    def __init__(self, name, active):
        self.name = name
        self.active = active

    def __repr__(self):
        return f"{self.id}"


class StatisticSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Statistic

    id = ma.auto_field()
    name = ma.auto_field()
    active = ma.auto_field()


statistic_schema = StatisticSchema()
statistics_schema = StatisticSchema(many=True)