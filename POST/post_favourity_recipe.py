from flask import Blueprint, jsonify, request

from db import get_connection

post_favourity_recipe_blueprint = Blueprint('post_favourity_recipe', __name__)

@post_favourity_recipe_blueprint.route('/api/v1/favourite_recipes', methods=['POST'])
def add_favourity_recipe():
    global conn, cur
    try:
        conn = get_connection()
        cur = conn.cursor()

        data = request.json

        client_id = data['client_id']
        recipe_id = data['recipe_id']

        cur.execute(f'INSERT INTO favourity_recipe(client_id, recipe_id) VALUES ({client_id}, {recipe_id})')

        conn.commit()

        return jsonify({'message': 'ok'})
    except:
        return jsonify({'message': 'error'})
    finally:
        cur.close()
        conn.close()