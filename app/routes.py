from flask import Blueprint
from app import db
from app.models.planet import Planet
from flask import request
from flask import request, make_response
from flask import jsonify

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")
@planets_bp.route("", methods=["POST"], strict_slashes=False)
def planets():

    request_body = request.get_json()
    new_planet = Planet(name = request_body["name"], 
                                description = request_body["description"],
                                diameter = request_body["diameter"])
    
    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

@planets_bp.route("", methods=["GET"], strict_slashes=False)
def all_planets():
    planets = Planet.query.all()
    planets_response = []
    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "diameter": planet.diameter
        })

    return jsonify(planets_response)


    
