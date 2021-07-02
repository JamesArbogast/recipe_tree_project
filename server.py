from flask_app import app
from flask_app.models.recipe_model import Recipe
from flask_app.controllers import routes_controller, family_controller, user_controller, login_reg_controller, recipe_controller






















if __name__ == "__main__":
    app.run(debug=True)