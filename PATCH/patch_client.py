import base64

from flask import Blueprint, jsonify, request
from github import Github

from POST.post_client import generate_random_filename
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
            encoded_image = data['image_path']

            image_bytes = base64.b64decode(encoded_image)

            github_token = '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'
            g = Github(github_token)

            repo = g.get_user().get_repo('kartinki')

            file_name = generate_random_filename(16) + '.png'

            full_path = 'https://github.com/koiikf/kartinki/blob/main/users/' + file_name
            information[4] = full_path

            repo.create_file('users/' + file_name, 'Add file', image_bytes)


        cur.execute('UPDATE client '
                    f"SET surname='{information[0]}', name='{information[1]}', patronymic='{information[2]}', "
                    f"phone='{information[3]}', image_path='{information[4]}' "
                    f'WHERE client_id={client_id}')

        conn.commit()


        cur.close()
        conn.close()

        return jsonify({'message': 'ok'})