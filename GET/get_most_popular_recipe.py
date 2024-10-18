from flask import Blueprint, jsonify

from db import get_connection

get_most_popular_recipe_blueprint = Blueprint('most_popular_recipe', __name__)

@get_most_popular_recipe_blueprint.route('/api/v1/most_popular_recipe')
def get_most_popular_recipe():
    global conn, cur
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute('SELECT * FROM recipe '
                    'WHERE recipe_id = ('
                    '   SELECT recipe_id FROM favourity_recipe '
                    '   GROUP BY recipe_id'
                    '   ORDER BY COUNT(*) DESC '
                    '   LIMIT 1'
                    ');'
        )

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
    except:
        return jsonify({'message': 'error'})
    finally:
        cur.close()
        conn.close()