from flask import request, jsonify, make_response
from marshmallow import ValidationError

from server.app import app, db
from server.models.stadium import stadium_schema, Stadium, stadiums_schema


@app.route('/stadiums', methods=["GET"])
def list_stadiums():
    records = db.paginate(Stadium.query)
    stadiums = stadiums_schema.dump(records)
    return make_response(stadiums, 200)



@app.route('/stadiums', methods=["POST"])
def create_stadium():
    json_data = request.get_json()
    data = stadium_schema.load(json_data)
    record = Stadium(**data)

    db.session.add(record)
    db.session.commit()

    return make_response({ "id": record.id }, 201)
