from flask import Blueprint, jsonify

from db import get_connection

get_recipes = Blueprint('get_recipes', __name__)

@get_recipes.route('/api/v1/recipes')
def get_recipes():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute('SELECT * FROM recipe')

    recipes = cur.fetchall()

    recipes_json = []
    for recipe in recipes:
        recipes_json.append(
            {
                'id': recipe[0],
                'title': recipe[1],
                'callories': recipe[2],
                'cooking_time': recipe[3],
                'complexity': recipe[4],
                'description': recipe[5],
                'image_path': recipe[6],
                'date': recipe[7]
            }
        )

    return jsonify(recipes_json)


@app.route('/api/v1/recipes/<int:recipe_id>')
def get_one_recipe(recipe_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(f'SELECT * FROM recipe WHERE recipe_id={recipe_id}')

    recipe = cur.fetchone()

    recipe_json = {
        'id': recipe[0],
        'title': recipe[1],
        'callories': recipe[2],
        'cooking_time': recipe[3],
        'complexity': recipe[4],
        'description': recipe[5],
        'image_path': recipe[6],
        'date': recipe[7]
    }

    return jsonify(recipe_json)