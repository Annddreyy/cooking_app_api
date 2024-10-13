from flask import Blueprint, jsonify

from db import get_connection

get_authorization_info_blueprint = Blueprint('get_authorization_info', __name__)

@get_authorization_info_blueprint.route('/api/v1/authorization')
def get_authorization_info():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute('SELECT client_id, email, password FROM client')

    information = cur.fetchall()

    information_json = []
    for info in information:
        information_json.append(
            {
                'id': info[0],
                'email': info[1],
                'password': info[2]
            }
        )

    return jsonify(information_json)
