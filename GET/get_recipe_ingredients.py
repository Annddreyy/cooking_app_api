from flask import Blueprint, jsonify

from db import get_connection

get_recipe_ingredients_blueprint = Blueprint('get_recipe_ingredients', __name__)

@get_recipe_ingredients_blueprint.route('/api/v1/recipe_ingredients/<int:recipe_id>', methods=['GET'])
def get_recipe_ingredients(recipe_id):
    global conn, cur
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(f'SELECT ingredient_id FROM recipe_ingredient WHERE recipe_id={recipe_id}')

        ingredients_id = cur.fetchall()

        ingredient_titles_json = []

        for ingredient_id in ingredients_id:
            cur.execute(f'SELECT title, count FROM ingredient WHERE ingredient_id={ingredient_id[0]}')

            ingredient = cur.fetchone()

            ingredient_titles_json.append(
                {
                    'id': ingredient_id[0],
                    'title': ingredient[0],
                    'count': ingredient[1]
                }
            )

        return jsonify(ingredient_titles_json)
    except:
        return jsonify({'message': 'error'})
    finally:
        cur.close()
        conn.close()
