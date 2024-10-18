from flask import Blueprint, jsonify, request

from db import get_connection

delete_favourity_recipe_blueprint = Blueprint('get_favourity_recipe', __name__)

@delete_favourity_recipe_blueprint.route('/api/v1/favourity_recipes', methods=['DELETE'])
def delete_favourity_recipe():
    global conn, cur
    try:
        conn = get_connection()
        cur = conn.cursor()

        data = request.json

        cur.execute(f'DELETE FROM favourity_recipe WHERE client_id={data['client_id']} AND recipe_id={data['recipe_id']}')

        conn.commit()

        return jsonify({'message': 'ok'})
    except:
        return jsonify({'message': 'error'})
    finally:
        cur.close()
        conn.close()