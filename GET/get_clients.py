from flask import Blueprint, jsonify

from db import get_connection


get_clients_blueprint = Blueprint('get_clients', __name__)


@get_clients_blueprint.route('/api/v1/clients')
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