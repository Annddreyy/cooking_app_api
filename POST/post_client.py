import base64
import random
import string

from flask import Blueprint, request, jsonify
from github import Github

from add_image_github import create_image
from db import get_connection

post_client_blueprint = Blueprint('post_client', __name__)

@post_client_blueprint.route('/api/v1/client', methods=['POST'])
def post_client():
    global conn, cur
    try:
        conn = get_connection()
        cur = conn.cursor()

        client = request.json

        full_path = create_image(client['image_path'], 'users/')

        cur.execute('INSERT INTO client(surname, name, patronymic, phone, email, image_path, password) '
                    f"VALUES ('{client['surname']}', '{client['name']}', '{client['patronymic']}', "
                    f"'{client['phone']}', '{client['email']}', '{full_path}',"
                    f"'{client['password']}')")

        conn.commit()

        cur.execute(f"SELECT client_id FROM client WHERE email='{client['email']}' AND password='{client['password']}';")
        id = cur.fetchone()[0]


        return {'id': id}
    except:
        return jsonify({'message': 'error'})
    finally:
        cur.close()
        conn.close()

