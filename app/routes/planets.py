from flask import Blueprint, jsonify

class Planet():
    def __init__(self,id,name, description):
        self.id = id
        self.name = name
        self.description = description
        
planets = [
    Planet(1,"Earth","Third planet from the sun"),
    Planet(2,"Moon", "Earth's only natural satellite"),
    Planet(3,"Mars","Fourth planet from the sun"),
    Planet(4,"Venus","Second planet from the sun, sometimes called Earth sister"),
    Planet(5,"Mercury","First planet from the sun, also the smalles planet in solar system")
        
]
planets_bp = Blueprint("planets",__name__,url_prefix="/planets")

@planets_bp.route('',methods=['GET'])
def get_all_planets():
    result = []
    for planet in planets:
        planet_dict = {"id": planet.id, "name": planet.name, "description": planet.description}
        result.append(planet_dict)
    return jsonify(result),200

@planets_bp.route('/<planet_id>',methods=['GET'])
def get_one_planets(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        return jsonify({"message": f"invalid data type {planet_id} id"}),400
    
    
    one_planet = None
    # planet_id = int(planet_id)
    for planet in planets:
        if planet.id == planet_id:
            one_planet = planet
    
    if one_planet is None:
        return jsonify({"message":f"Could not find planet with id: {planet_id}"}), 404
    
    return_planet = {
        "id": one_planet.id,
        "name": one_planet.name,
        "description": one_planet.description        
    }
    
    return jsonify(return_planet), 200
    
    