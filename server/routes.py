from flask import Blueprint, jsonify, request
from server.models import db
from server.models.pizza import Pizza
from server.models.restaurant import Restaurant
from server.models.restaurant_pizza import RestaurantPizza

api = Blueprint('api', __name__)
@api.route("/pizzas", methods=["GET"])
def get_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([{
        "id": pizza.id,
        "name": pizza.name,
        "ingredients": pizza.ingredients
    } for pizza in pizzas]), 200


@api.route("/restaurants", methods=["GET"])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([{
        "id": r.id,
        "name": r.name,
        "address": r.address
    } for r in restaurants]), 200


@api.route("/restaurants/<int:id>", methods=["GET"])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404

    return jsonify({
        "id": restaurant.id,
        "name": restaurant.name,
        "address": restaurant.address,
        "pizzas": [
            {
                "id": rp.pizza.id,
                "name": rp.pizza.name,
                "ingredients": rp.pizza.ingredients,
                "price": rp.price
            }
            for rp in restaurant.restaurant_pizzas
        ]
    }), 200

@api.route("/restaurants/<int:id>", methods=["DELETE"])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404

    db.session.delete(restaurant)
    db.session.commit()
    return '', 204

@api.route("/pizzas/<int:id>", methods=["DELETE"])
def delete_pizza(id):
    pizza = Pizza.query.get(id)
    if not pizza:
        return jsonify({"error": "Pizza not found"}), 404

    db.session.delete(pizza)
    db.session.commit()
    return '', 204



@api.route("/restaurants", methods=["POST"])
def create_restaurant():
    data = request.get_json()
    try:
        new_restaurant = Restaurant(name=data["name"], address=data["address"])
        db.session.add(new_restaurant)
        db.session.commit()
        return jsonify({
            "id": new_restaurant.id,
            "name": new_restaurant.name,
            "address": new_restaurant.address
        }), 201
    except Exception as e:
        return jsonify({"error": "Invalid data"}), 400


@api.route("/pizzas", methods=["POST"])
def create_pizza():
    data = request.get_json()
    try:
        new_pizza = Pizza(name=data["name"], ingredients=data["ingredients"])
        db.session.add(new_pizza)
        db.session.commit()
        return jsonify({
            "id": new_pizza.id,
            "name": new_pizza.name,
            "ingredients": new_pizza.ingredients
        }), 201
    except Exception as e:
        return jsonify({"error": "Invalid data"}), 400


@api.route("/restaurant_pizzas", methods=["POST"])
def add_pizza_to_restaurant():
    data = request.get_json()
    try:
        price = int(data["price"])
        if price < 1 or price > 30:
            raise ValueError("Price must be between 1 and 30")

        rp = RestaurantPizza(
            price=price,
            pizza_id=data["pizza_id"],
            restaurant_id=data["restaurant_id"]
        )
        db.session.add(rp)
        db.session.commit()

        pizza = Pizza.query.get(rp.pizza_id)
        return jsonify({
            "id": pizza.id,
            "name": pizza.name,
            "ingredients": pizza.ingredients
        }), 201

    except Exception as e:
        return jsonify({"errors": ["validation errors"]}), 400
