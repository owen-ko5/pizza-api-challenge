# 🍕 PIZZA RESTAURANT API

Welcome to the **Pizza Restaurant API** — a RESTful Flask application that lets users view, add, associate, and delete restaurants and pizzas! Perfect for building out backend CRUD functionality with Python, Flask, and SQLAlchemy.

---

## 📦 TECHNOLOGIES USED

- 🐍 Python 3.8+
- ⚙️ Flask
- 🛠️ Flask-Migrate
- 🗄️ SQLAlchemy (ORM)
- 📫 Postman (for API testing)

---

## 📁 PROJECT STRUCTURE

Pizza-Restaurants/
│
├── server/
│ ├── app.py # Main application factory
│ ├── config.py # Configuration settings
│ ├── routes.py # All API endpoints
│ ├── seed.py # Seed data for testing
│ └── models/
│ ├── init.py # DB init
│ ├── pizza.py # Pizza model
│ ├── restaurant.py # Restaurant model
│ └── restaurant_pizza.py # Association model
│
├── migrations/ # Auto-generated by Flask-Migrate
├── venv/ # Python virtual environment
└── README.md #



## 🔌 Setup Instructions

1. **Clone the repository**:
   git clone https://github.com/your-username/Pizza-Restaurants.git
   cd Pizza-Restaurants

CREATE AND ACTIVATE YOUR VIRTUAL ENVIRONMENT
python3 -m venv venv
source venv/bin/activate

INSTALL DEPENDENCIES
pip install -r requirements.txt
SET THE FLASK APP:
export FLASK_APP=server/app.py

Initialize and migrate database:
flask db init
flask db migrate -m "Initial"
flask db upgrade

Seed the database (optional):
python server/seed.py

START THE DEVELOPMENT SERVER:
flask run


🧪 API Endpoints
Method	Endpoint	Description
GET	/pizzas	Get all pizzas 🍕
POST	/pizzas	Create a new pizza
DELETE	/pizzas/<id>	Delete a pizza by ID
GET	/restaurants	Get all restaurants 🏬
POST	/restaurants	Create a new restaurant
GET	/restaurants/<id>	Get a restaurant and its pizzas
DELETE	/restaurants/<id>	Delete a restaurant by ID
POST	/restaurant_pizzas	Link a pizza to a restaurant 🍕🏬


📬 SAMPLE JSON PAYLOADS
Create a Pizza
POST /pizzas
{
  "name": "Margherita",
  "ingredients": "Tomato, Mozzarella, Basil"
}

Create a Restaurant
POST /restaurants
{
  "name": "Slice Heaven",
  "address": "123 Dough Street"
}

ADD PIZZA TO RESTAURANT
POST /restaurant_pizzas
{
  "price": 15,
  "pizza_id": 1,
  "restaurant_id": 2
}

💡 TIPS
Test endpoints using Postman or cURL.

Ensure your virtual environment is always activated when working.

Use flask db migrate anytime you change your models.


🧼 License
This project is licensed under the MIT License.
Feel free to use, modify, and distribute! 🌍

Let me know if you'd like this in a downloadable file or want to add badges (like Build # pizza-restaurant-code-challenge
