from flask import Blueprint, request, jsonify
from server.models.restaurant import Restaurant
from server.models import db

restaurant_bp = Blueprint('restaurants', __name__)
@restaurant_bp.route('/restaurants', methods=['POST'])
def create_restaurant():
    data = request.get_json()
    try:
        new_restaurant = Restaurant(name=data['name'], address=data['address'])
        db.session.add(new_restaurant)
        db.session.commit()
        return jsonify({
            "id": new_restaurant.id,
            "name": new_restaurant.name,
            "address": new_restaurant.address
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@restaurant_bp.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant:
        db.session.delete(restaurant)
        db.session.commit()
        return '', 204
    else:
        return jsonify({"error": "Restaurant not found"}), 404
