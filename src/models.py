from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship


db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    """ favorite_planet = db.relationship('Favorite_planet', lazy=True) """

    def __repr__(self):
        return '<User %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class Peoples(db.Model):
    __tablename__ = 'peoples'
    id = db.Column(db.Integer, primary_key=True)
    people_name = db.Column(db.String(120), unique=True, nullable=False)
    birth_year = db.Column(db.String(80), unique=False, nullable=False)
    gender = db.Column(db.String(80), unique=False, nullable=False)
    height = db.Column(db.String(80), unique=False, nullable=False)
    skin_color = db.Column(db.String(80), unique=False, nullable=False)
    eye_color = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return '<Peoples %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "people_name": self.people_name,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "height": self.height,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color
            # do not serialize the password, its a security breach
        }


class Planets(db.Model):
    """ __tablename__ = 'planets' """
    id = db.Column(db.Integer, primary_key=True)
    planet_name = db.Column(db.String(120), unique=True, nullable=False)
    climate = db.Column(db.String(80), unique=False, nullable=False)
    population = db.Column(db.String(80), unique=False, nullable=False)
    orbital_period = db.Column(db.String(80), unique=False, nullable=False)
    rotation_period = db.Column(db.String(80), unique=False, nullable=False)
    diameter = db.Column(db.String(80), unique=False, nullable=False)
    """ favorite_planet = db.relationship('Favorite_planet', lazy=True) """

    def __repr__(self):
        return '<Planets %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "planet_name": self.planet_name,
            "climate": self.climate,
            "population": self.population,
            "orbital_period": self.orbital_period,
            "rotation_period": self.rotation_period,
            "diameter": self.diameter,
            
            # do not serialize the password, its a security breach
        }


class Favorite_planet(db.Model):
    __tablename__ = 'favorite_planet'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    planets_id = db.Column(db.Integer,  db.ForeignKey('planets.id'))
    planet_name = db.Column(db.String(120), unique=True, nullable=False)
    #user = db.relationship(User)
    #planet = db.relationship(Planets)
    

    def __repr__(self):
        return '<Favorite_planet %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,           
            "planet_name": self.name,
            "user_id": self.user_id,
            "planets_id": self.planets_id,
            # do not serialize the password, its a security breach
        }


class Favorite_people(db.Model):
    __tablename__ = 'favorite_people'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    peoples_id = db.Column(db.Integer,  db.ForeignKey('peoples.id'))
    people_name = db.Column(db.String(120), unique=True, nullable=False)
    #user = db.relationship(User)
    #people = db.relationship(Peoples)

    def __repr__(self):
        return '<Favorites_people %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "people_name": self.people_name,
            "user_id": self.user_id,
            "peoples_id": self.peoples_id,
            # do not serialize the password, its a security breach
        }
