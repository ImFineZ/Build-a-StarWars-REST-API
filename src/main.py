"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Planets, Peoples, Favorite_people, Favorite_planet
# from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object


@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints


@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/user', methods=['GET'])
def get_user():
    users = User.query.filter().all()
    result = list(map(lambda user: user.serialize(), users))
    response_body = {
        "Usuarios": result,
        "msg": "Hello, this is your GET /user response "
    }
    return jsonify(response_body), 200


@app.route("/people", methods=["GET"])
def get_peoples():
    peoples = Peoples.query.filter().all()
    result = list(map(lambda people: people.serialize(), peoples))
    response_body = {
        "Usuarios": result,
        "msg": "Hello, this is your GET /people response"
    }
    return jsonify(response_body), 200


@app.route('/people/<int:people_id>', methods=['GET'])
def get_people(people_id):
    people = Peoples.query.get(people_id)
    response_body = {
       "people": people
    }
    return jsonify(people.serialize()), 200


@app.route("/planet", methods=["GET"])
def get_planets():
    planets = Planets.query.filter().all()
    result = list(map(lambda planet: planet.serialize(), planets))
    response_body = {
        "Usuarios": result,
        "msg": "Hello, this is your GET /planet response "
    }
    return jsonify(response_body), 200


@app.route('/planet/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):
    planet = Planets.query.get(planet_id)
    return jsonify(planet.serialize()), 200


@app.route('/user/<int:user_id>/addfavoriteplanet/<int:planets_id>/', methods=['POST'])
def add_planet(user_id, planets_id):
    usuario_query = User.query.get(user_id)
    fav_planet = Favorite_planet(
        user_id=usuario_query.id, planets_id=int(planets_id))
    db.session.add(fav_planet)
    db.session.commit()
    response_body = {"msg": "Favorito agregado"}
    return jsonify(response_body), 200

    """ fav_people = Favorites_people(user_id=int(user_id), people_id=int(people_id))
    db.session.add(fav_people)
    db.session.commit()
    response_body = {"msg": "Favorito agregado"}
    return jsonify(response_body), 200 """


@app.route('/user/<int:user_id>/addfavoritepeople/<int:peoples_id>/', methods=['POST'])
def add_people(user_id, peoples_id):
    usuario_query = User.query.get(user_id)
    fav_people = Favorite_people(
        user_id=usuario_query.id, peoples_id=int(peoples_id))
    db.session.add(fav_people)
    db.session.commit()
    response_body = {"msg": "Favorito agregado"}
    return jsonify(response_body), 200

@app.route('/user/<int:user_id>/deletefavoriteplanet/<int:planets_id>/', methods=['DELETE'])
def delete_favoriteplanet(user_id, planets_id):
    delete = Favorite_planet.query.filter_by(
        planets_id=planets_id, user_id=user_id).first()
    db.session.delete(delete)
    db.session.commit()
    return jsonify({"msg": "Deleted planet"}), 200


@app.route('/user/<int:user_id>/deletefavoritepeople/<int:peoples_id>/', methods=['DELETE'])
def delete_favoritepeople(user_id, peoples_id):
    delete = Favorite_people.query.filter_by(
        peoples_id=peoples_id, user_id=user_id).first()
    db.session.delete(delete)
    db.session.commit()
    return jsonify({"msg": "Deleted planet"}), 200

# ****Para agregar los favoritos de usuario especifico****
""" @app.route("/user/<int:user_id>/favorites", methods=["GET"])
def get_favorites(user_id):
planets = Favorites_planet.query.filter_by(user_id=user_id).all()
people = Favorites_people.query.filter_by(user_id=user_id).all()
vehicles = Favorites_vehicles.query.filter_by(user_id=user_id).all()
result = (list(map(lambda planet: planet.serialize(), planets)),
list(map(lambda character: character.serialize(), people)),
list(map(lambda vehicle: vehicle.serialize(), vehicles)))
return jsonify(result), 200 """

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
