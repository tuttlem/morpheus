from server.app import db, ma


class Stadium(db.Model):
    __tablename__ = 'stadium'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), required=True)
    location = db.Column(db.String(80), required=True)
    image = db.Column(db.String(80), required=True)

    def __init__(self, name, location, image):
        self.name = name
        self.location = location
        self.image = image

    def __repr__(self):
        return f"{self.id}"


class StadiumSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Stadium

    id = ma.auto_field()
    name = ma.auto_field()
    location = ma.auto_field()
    image = ma.auto_field()


stadium_schema = StadiumSchema()
stadiums_schema = StadiumSchema(many=True)