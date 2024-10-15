from flask import Blueprint, jsonify

from db import get_connection

get_recipe_with_recipe_type_blueprint = Blueprint('recipe_with_recipe_type_blueprint', __name__)

@get_recipe_with_recipe_type_blueprint.route('/api/v1/recipe_with_recipe_type/<int:recipe_type_id>')
def get_recipe_with_recipe_type(recipe_type_id):
    global conn, cur
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(f'SELECT recipe_id FROM recipe_recipe_type WHERE recipe_type_id={recipe_type_id}')

        all_recipes = cur.fetchall()
        recipes = []
        for recipe in all_recipes:
            recipes.append(recipe[0])

        return jsonify({'recipes': recipes})
    except:
        return jsonify({'message': 'error'})
    finally:
        cur.close()
        conn.close()