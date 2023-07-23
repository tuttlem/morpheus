from server.app import db, ma


class Player(db.Model):
    __tablename__ = 'player'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    location = db.Column(db.String(80), nullable=False)
    image = db.Column(db.String(80), nullable=False)


    def __init__(self, first_name, last_name, location, image):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.image = image

    def __repr__(self):
        return f"{self.id}"


class PlayerSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Player

    id = ma.auto_field()
    first_name = ma.auto_field()
    last_name = ma.auto_field()
    location = ma.auto_field()
    image = ma.auto_field()


player_schema = PlayerSchema()
players_schema = PlayerSchema(many=True)