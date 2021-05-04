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

    return make_response(jsonify(f"Planet {new_planet.name} successfully created"), 201)

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

@planets_bp.route("/<planet_id>", methods=["GET", "PUT", "DELETE"], strict_slashes=False)

def manage_planet(planet_id):
    planet = Planet.query.get(planet_id)

    if planet is None:
        return ({
        "message": f"Planet with id {planet_id} was not found",
        "success": False,
    }, 404)

    if request.method == "GET":

        return ({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "diameter": planet.diameter
        }, 200)

    elif request.method == "PUT":
        form_data = request.get_json()

        planet.name = form_data["name"]
        planet.description = form_data["description"]
        planet.diameter = form_data["diameter"]

        db.session.commit()

        return make_response(f"Planet #{planet.id} successfully updated")

    elif request.method == "DELETE":
        db.session.delete(planet)
        db.session.commit()
        return make_response(f"Planet #{planet.id} successfully deleted")