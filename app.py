from flask import Flask, jsonify

from db import get_connection

app = Flask(__name__)

@app.route('/api/v1/clients')
def get_clients():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute('SELECT * FROM client')

    clients = cur.fetchall()

    clients_json = []
    for client in clients:
        clients_json.append(
            {
                'id': client[0],
                'surname': client[1],
                'name': client[2],
                'patronymic': client[3],
                'phone': client[4],
                'image_path': client[5],
                'email': client[6],
                'password': client[7]
            }
        )

    cur.close()
    conn.close()

    return jsonify(clients_json)


@app.route('/api/v1/recipes')
def get_recipes():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute('SELECT * FROM recipe')

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


@app.route('/api/v1/recipes/<int:recipe_id>')
def get_one_recipe(recipe_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(f'SELECT * FROM recipe WHERE recipe_id={recipe_id}')

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


@app.route('/api/v1/recipe_types')
def get_recipe_types():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute('SELECT * FROM recipe_type')

    recipe_types = cur.fetchall()

    recipe_types_json = []
    for recipe_type in recipe_types:
        recipe_types_json.append(
            {
                'id': recipe_type[0],
                'title': recipe_type[1],
                'image_path': recipe_type[2],
            }
        )

    return jsonify(recipe_types_json)


if __name__ == '__main__':
    app.run(debug=True, port=1234)