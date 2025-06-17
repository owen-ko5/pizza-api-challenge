from flask import Blueprint, request, jsonify
from server.models.pizza import Pizza
from server.models import db

pizza_bp = Blueprint('pizzas', __name__)

@pizza_bp.route('/pizzas', methods=['POST'])
def create_pizza():
    data = request.get_json()
    try:
        new_pizza = Pizza(name=data['name'], ingredients=data['ingredients'])
        db.session.add(new_pizza)
        db.session.commit()
        return jsonify({
            "id": new_pizza.id,
            "name": new_pizza.name,
            "ingredients": new_pizza.ingredients
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
@pizza_bp.route('/pizzas/<int:id>', methods=['DELETE'])
def delete_pizza(id):
    pizza = Pizza.query.get(id)
    if pizza:
        db.session.delete(pizza)
        db.session.commit()
        return '', 204
    else:
        return jsonify({"error": "Pizza not found"}), 404
