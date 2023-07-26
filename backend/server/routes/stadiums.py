from flask import request, jsonify, make_response
from marshmallow import ValidationError

from server.app import app, db
from server.models.stadium import stadium_schema, Stadium, stadiums_schema


@app.route('/stadiums', methods=["GET"])
def list_stadiums():
    records = db.paginate(Stadium.query)
    stadiums = stadiums_schema.dump(records)
    return make_response(stadiums, 200)


@app.route('/stadiums/<stadium_id>', methods=["GET"])
def get_stadium(stadium_id):
    record = Stadium.query.get(stadium_id)
    stadium = stadium_schema.dump(record)
    return make_response(stadium, 200)


@app.route('/stadiums/<int:id>', methods=["PUT"])
def update_stadium(id):
    stadium = Stadium.query.get(id)

    if not stadium:
        return jsonify({'message': 'Stadium not found'}), 404

    updated_stadium_data = request.json
    errors = stadium_schema.validate(updated_stadium_data, partial=True)

    if errors:
        return jsonify(errors), 400

    for key, value in updated_stadium_data.items():
        setattr(stadium, key, value)

    db.session.commit()
    return stadium_schema.jsonify(stadium), 200


@app.route('/stadiums', methods=["POST"])
def create_stadium():
    json_data = request.get_json()
    data = stadium_schema.load(json_data)
    record = Stadium(**data)

    db.session.add(record)
    db.session.commit()

    return make_response({ "id": record.id }, 201)

