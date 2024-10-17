from flask import Blueprint, jsonify, request

from db import get_connection

patch_clients_blueprint = Blueprint('patch_client', __name__)

@patch_clients_blueprint.route('/api/v1/client/<int:client_id>', methods=['PATCH'])
def patch_client(client_id):
    global conn, cur
    try:
        conn = get_connection()
        cur = conn.cursor()

        data = request.json

        surname = data['surname']
        name = data['name']
        patronymic = data['patronymic']
        phone = data['phone']
        image_path = data['image_path']

        cur.execute('UPDATE client '
                    f'SET surname={surname}, name={name}, patronymic={patronymic}, '
                    f'phone={phone}, image_path={image_path}')

        conn.commit()

        return jsonify({'message': 'ok'})
    except:
        return jsonify({'message': 'error'})
    finally:
        cur.close()
        conn.close()