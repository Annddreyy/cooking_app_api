from flask import Blueprint, jsonify

from db import get_connection

get_recipe_instructions_blueprint = Blueprint('get_recipe_instructions', __name__)

@get_recipe_instructions_blueprint.route('/api/v1/recipe_instructions/<int:recipe_id>', methods=['GET'])
def get_recipe_instructions(recipe_id):
    global cur, conn
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(f'SELECT instruction_id FROM recipe_instruction WHERE recipe_id={recipe_id}')

        instructions_id = cur.fetchall()

        instructions_titles_json = []

        for instruction_id in instructions_id:
            cur.execute(f'SELECT text FROM instruction WHERE instruction_id={instruction_id[0]}')

            instruction = cur.fetchone()

            instructions_titles_json.append(
                {
                    'id': instruction_id[0],
                    'text': instruction[0]
                }
            )

        return jsonify(instructions_titles_json)
    except:
        return jsonify({'message': 'error'})
    finally:
        cur.close()
        conn.close()