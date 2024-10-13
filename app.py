from flask import Flask

from GET.get_authorization_info import get_authorization_info_blueprint
from GET.get_client import get_client_blueprint
from GET.get_recipe_ingredients import get_recipe_ingredients_blueprint
from GET.get_recipe_instructions import get_recipe_instructions_blueprint
from GET.get_recipe_types import get_recipe_types_blueprint
from GET.get_recipes import get_recipes_blueprint

app = Flask(__name__)


app.register_blueprint(get_client_blueprint)
app.register_blueprint(get_recipes_blueprint)
app.register_blueprint(get_recipe_types_blueprint)
app.register_blueprint(get_recipe_ingredients_blueprint)
app.register_blueprint(get_recipe_instructions_blueprint)
app.register_blueprint(get_authorization_info_blueprint)


if __name__ == '__main__':
    app.run(debug=True, port=1234)