from server.app import app
from server.models import db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

with app.app_context():
    print("Seeding database...")

    Restaurant.query.delete()
    Pizza.query.delete()
    RestaurantPizza.query.delete()
    r1 = Restaurant(name="Zen kitchen", address="1bazzer plaza")
    r2 = Restaurant(name="Pizza Inn", address="thika road")
    db.session.add_all([r1, r2])
    db.session.commit()

    p1 = Pizza(name="Chicken", ingredients="Tomato, Chicken")
    p2 = Pizza(name="Hawaian", ingredients="Pepperoni, pineaple")
    db.session.add_all([p1, p2])
    db.session.commit()

    rp1 = RestaurantPizza(price=10, pizza_id=p1.id, restaurant_id=r1.id)
    rp2 = RestaurantPizza(price=12, pizza_id=p2.id, restaurant_id=r2.id)
    db.session.add_all([rp1, rp2])
    db.session.commit()

    print("Done seeding!")
