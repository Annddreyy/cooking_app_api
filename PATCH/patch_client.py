from flask import Blueprint, jsonify, request

from add_image_github import create_image
from db import get_connection

patch_clients_blueprint = Blueprint('patch_client', __name__)

@patch_clients_blueprint.route('/api/v1/client/<int:client_id>', methods=['PATCH'])
def patch_client(client_id):
        conn = get_connection()
        cur = conn.cursor()

        data = request.json


        cur.execute(f'SELECT surname, name, patronymic, phone, image_path FROM client '
                    f'WHERE client_id={client_id}')

        information = list(cur.fetchone())


        if 'surname' in data:
            information[0] = data['surname']
        if 'name' in data:
            information[1] = data['name']
        if 'patronymic' in data:
            information[2] = data['patronymic']
        if 'phone' in data:
            information[3] = data['phone']
        if 'image_path' in data:
            full_path = create_image(data['image_path'], 'users/')
            information[4] = full_path


        cur.execute('UPDATE client '
                    f"SET surname='{information[0]}', name='{information[1]}', patronymic='{information[2]}', "
                    f"phone='{information[3]}', image_path='{information[4]}' "
                    f'WHERE client_id={client_id}')

        conn.commit()


        cur.close()
        conn.close()

        return jsonify({'message': 'ok'})