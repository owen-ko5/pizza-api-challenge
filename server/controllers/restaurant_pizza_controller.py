from flask import Blueprint, request, jsonify
from server.app import db
from server.models.restaurant_pizza import RestaurantPizza
from server.models.pizza import Pizza
from server.models.restaurant import Restaurant

restaurant_pizza_bp = Blueprint("restaurant_pizzas", __name__)

@restaurant_pizza_bp.route("/restaurant_pizzas", methods=["POST"])
def create_restaurant_pizza():
    data = request.get_json()

    try:
        price = int(data["price"])
        pizza_id = data["pizza_id"]
        restaurant_id = data["restaurant_id"]
    except (KeyError, ValueError):
        return jsonify({"errors": ["Invalid input"]}), 400

    rp = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)

    if not rp.is_valid_price():
        return jsonify({"errors": ["Price must be between 1 and 30"]}), 400

    db.session.add(rp)
    db.session.commit()

    return jsonify({
        "id": rp.id,
        "price": rp.price,
        "pizza_id": rp.pizza_id,
        "restaurant_id": rp.restaurant_id,
        "pizza": {
            "id": rp.pizza.id,
            "name": rp.pizza.name,
            "ingredients": rp.pizza.ingredients
        },
        "restaurant": {
            "id": rp.restaurant.id,
            "name": rp.restaurant.name,
            "address": rp.restaurant.address
        }
    }), 201
