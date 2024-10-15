import base64
import random
import string

from flask import Blueprint, request, jsonify
from github import Github

from db import get_connection

post_client_blueprint = Blueprint('post_client', __name__)

@post_client_blueprint.route('/api/v1/client', methods=['POST'])
def post_client():
    conn = get_connection()
    cur = conn.cursor()

    client = request.json

    encoded_image = client['image_path']

    image_bytes = base64.b64decode(encoded_image)

    github_token = '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'
    github_token = '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'
    g = Github(github_token)

    # Укажите репозиторий и пользователя
    repo = g.get_user().get_repo('kartinki')

    file_name = generate_random_filename(16) + '.png'

    full_path = 'https://github.com/koiikf/kartinki/blob/main/users/' + file_name


    # Создайте файл в репозитории
    repo.create_file('users/' + file_name, 'Add file', image_bytes)

    cur.execute('INSERT INTO client(surname, name, patronymic, phone, email, image_path, password) '
                f"VALUES ('{client['surname']}', '{client['name']}', '{client['patronymic']}', "
                f"'{client['phone']}', '{client['email']}', '{full_path}',"
                f"'{client['password']}')")

    conn.commit()

    cur.execute(f"SELECT client_id FROM client WHERE email='{client['email']}' AND password='{client['password']}';")
    id = cur.fetchone()[0]

    cur.close()
    conn.close()



    return {'id': id}


def generate_random_filename(length=16):
    characters = string.hexdigits + string.digits
    return ''.join(random.choice(characters) for _ in range(length))
