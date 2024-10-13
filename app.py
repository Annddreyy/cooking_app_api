from flask import Flask

from GET.get_clients import get_clients
from GET.get_recipe_types import get_recipe_types
from GET.get_recipes import get_recipes

app = Flask(__name__)


app.register_blueprint(get_clients)
app.register_blueprint(get_recipes)
app.register_blueprint(get_recipe_types)


if __name__ == '__main__':
    app.run(debug=True, port=1234)