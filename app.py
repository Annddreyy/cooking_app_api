from flask import Flask

from DELETE.delete_favourity_recipe import delete_favourity_recipe_blueprint
from GET.get_authorization_info import get_authorization_info_blueprint
from GET.get_client import get_client_blueprint
from GET.get_favourite_recipes import get_favourite_recipes_blueprint
from GET.get_recipe_ingredients import get_recipe_ingredients_blueprint
from GET.get_recipe_instructions import get_recipe_instructions_blueprint
from GET.get_recipe_types import get_recipe_types_blueprint
from GET.get_recipe_with_recipe_type import get_recipe_with_recipe_type_blueprint
from GET.get_recipes import get_recipes_blueprint
from POST.post_client import post_client_blueprint
from POST.post_favourity_recipe import post_favourity_recipe_blueprint

app = Flask(__name__)


app.register_blueprint(get_client_blueprint)
app.register_blueprint(get_recipes_blueprint)
app.register_blueprint(get_recipe_types_blueprint)
app.register_blueprint(get_recipe_ingredients_blueprint)
app.register_blueprint(get_recipe_instructions_blueprint)
app.register_blueprint(get_authorization_info_blueprint)
app.register_blueprint(get_recipe_with_recipe_type_blueprint)
app.register_blueprint(get_favourite_recipes_blueprint)

app.register_blueprint(post_client_blueprint)
app.register_blueprint(post_favourity_recipe_blueprint)

app.register_blueprint(delete_favourity_recipe_blueprint)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)