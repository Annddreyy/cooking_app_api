from flask import Flask, jsonify

from db import get_connection

app = Flask(__name__)

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
                'cooking_time': recipe[3]
            }
        )

    cur.close()
    conn.close()

    return jsonify(recipes_json)


if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=80)