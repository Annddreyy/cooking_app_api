from flask import Blueprint, jsonify

from db import get_connection

get_recipe_types = Blueprint('recipe_types', __name__)

@get_recipe_types.route('/api/v1/recipe_types')
def get_recipe_types():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute('SELECT * FROM recipe_type')

    recipe_types = cur.fetchall()

    recipe_types_json = []
    for recipe_type in recipe_types:
        recipe_types_json.append(
            {
                'id': recipe_type[0],
                'title': recipe_type[1],
                'image_path': recipe_type[2],
            }
        )

    return jsonify(recipe_types_json)