from flask import Blueprint, jsonify

from db import get_connection


get_client_blueprint = Blueprint('get_client', __name__)


@get_client_blueprint.route('/api/v1/client/<int:client_id>', methods=['GET'])
def get_clients(client_id):
    global conn, cur
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute('SELECT surname, name, patronymic, phone, image_path FROM client '
                    f'WHERE client_id={client_id}')

        client = cur.fetchone()
        if client:
            clients_json = {
                'surname': client[0],
                'name': client[1],
                'patronymic': client[2],
                'phone': client[3],
                'image_path': client[4]
            }
            return jsonify(clients_json)
        else:
            return jsonify({'message': 'no object with this id'})
    except:
        return jsonify({'message': 'error'})
    finally:
        cur.close()
        conn.close()