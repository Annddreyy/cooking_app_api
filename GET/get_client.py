from flask import Blueprint, jsonify

from db import get_connection


get_client_blueprint = Blueprint('get_client', __name__)


@get_client_blueprint.route('/api/v1/client/<int:client_id>')
def get_clients(client_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute('SELECT surname, name, patronymic, phone, image_path FROM client '
                f'WHERE client_id={client_id}')

    client = cur.fetchone()

    clients_json = {
        'surname': client[0],
        'name': client[1],
        'patronymic': client[2],
        'phone': client[3],
        'image_path': client[4]
    }

    cur.close()
    conn.close()

    return jsonify(clients_json)