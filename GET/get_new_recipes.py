from flask import Blueprint, jsonify

from GET.get_recipes import get_recipes_blueprint
from db import get_connection

get_new_recipes_blueprint = Blueprint('get_new_recipe', __name__)
@get_recipes_blueprint.route('/api/v1/new_recipes')
def get_new_recipes():
    global conn, cur
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute('SELECT * FROM recipe')

        recipes = cur.fetchall()

        recipes = sorted(recipes, key=lambda item: item[-1], reverse=True)[:5]

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
    except:
        return jsonify({'message': 'error'})
    finally:
        cur.close()
        conn.close()