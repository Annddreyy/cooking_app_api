from flask import Blueprint, jsonify

from db import get_connection

get_favourite_recipes_blueprint = Blueprint('get_favourite_recipes', __name__)

@get_favourite_recipes_blueprint.route('/api/v1/favourite_recipes/<int:client_id>')
def get_favourite_recipes(client_id):
    global cur, conn
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(f'SELECT recipe_id FROM favourity_recipe WHERE client_id={client_id}')

        recipe_ids = cur.fetchall()

        recipes_json = []
        for recipe_id in recipe_ids:
            cur.execute(f'SELECT * FROM recipe WHERE recipe_id={recipe_id[0]}')
            recipe = cur.fetchone()
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
