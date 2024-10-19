from flask import Blueprint, jsonify

from db import get_connection

get_user_recipe_blueprint = Blueprint('get_user_recipe', __name__)

@get_user_recipe_blueprint.route("/api/v1/user_recipes/<int:client_id>", methods=['GET'])
def get_user_recipes(client_id):
    global conn, cursor
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute('SELECT * FROM recipe '
                    'WHERE recipe_id IN ('
                    '   SELECT recipe_id FROM recipe_of_client '
                    f'   WHERE client_id={client_id}'
                    f')')

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
    except:
        return jsonify({'message': 'error'})
    finally:
        cur.close()
        conn.close()
