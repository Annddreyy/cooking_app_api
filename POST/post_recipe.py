from datetime import datetime

from flask import Blueprint, jsonify, request

from add_image_github import create_image
from db import get_connection

post_recipe_blueprint = Blueprint('post_recipe', __name__)

@post_recipe_blueprint.route('/api/v1/recipe', methods=['POST'])
def post_recipe():
    global conn, cur
    try:
        conn = get_connection()
        cur = conn.cursor()

        recipe_data = request.json

        title = recipe_data['title']
        callories = recipe_data['callories']
        cooking_time = recipe_data['time']
        complexity = recipe_data['complexity']
        description = recipe_data['description']
        client_id = recipe_data['client_id']

        image_path = create_image(recipe_data['image_path'], 'recipes/')
        now = datetime.now()
        formatted_date = now.strftime('%Y-%m-%d')

        cur.execute('INSERT INTO recipe(title, callories, cooking_time, '
                    'complexity, description, image_path, date, is_user_recipe) '
                    f"VALUES('{title}', '{callories}', '{cooking_time}', '{complexity}', "
                    f"'{description}', '{image_path}', '{formatted_date}', 2)")
        conn.commit()

        cur.execute('SELECT recipe_id FROM recipe ORDER BY recipe_id DESC LIMIT 1')
        recipe_id = cur.fetchone()[0]

        cur.execute(f'INSERT INTO recipe_of_client(client_id, recipe_id) VALUES({client_id}, {recipe_id})')

        ingredients_data = recipe_data['ingredients']
        for ingredient in ingredients_data:
            cur.execute(f"INSERT INTO ingredient(title, count) VALUES('{ingredient[0]}', '{ingredient[1]}')")
            conn.commit()

            cur.execute('SELECT ingredient_id FROM ingredient ORDER BY ingredient_id DESC LIMIT 1')
            ingredient_id = cur.fetchone()[0]

            cur.execute(f"INSERT INTO recipe_ingredient VALUES ({recipe_id}, {ingredient_id})")
            conn.commit()

        instructions_data = recipe_data['instructions']
        for instruction in instructions_data:
            cur.execute(f"INSERT INTO instruction(text) VALUES('{instruction}')")
            conn.commit()

            cur.execute('SELECT instruction_id FROM instruction ORDER BY instruction_id DESC LIMIT 1')
            instruction_id = cur.fetchone()[0]

            cur.execute(f"INSERT INTO recipe_instruction VALUES ({recipe_id}, {instruction_id})")
            conn.commit()

        recipe_types_data = recipe_data['recipe_types']
        for recipe_type in recipe_types_data:
            cur.execute(f"SELECT recipe_type_id FROM recipe_type WHERE title='{recipe_type}'")
            recipe_type_id = cur.fetchone()[0]
            cur.execute(f'INSERT INTO recipe_recipe_type(recipe_id, recipe_type_id) VALUES ({recipe_id}, {recipe_type_id})')
            conn.commit()

        return jsonify({'message': 'ok'})
    except:
        return jsonify({'message': 'error'})
    finally:
        cur.close()
        conn.close()

