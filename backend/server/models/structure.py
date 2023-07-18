from server.app import db, ma


class Structure(db.Model):
    __tablename__ = 'structure'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), required=True)
    active = db.Column(db.Boolean, required=True)

    def __init__(self, name, active):
        self.name = name
        self.active = active

    def __repr__(self):
        return f"{self.id}"


class StructureSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Structure

    id = ma.auto_field()
    name = ma.auto_field()
    active = ma.auto_field()


structure_schema = StructureSchema()
structures_schema = StructureSchema(many=True)