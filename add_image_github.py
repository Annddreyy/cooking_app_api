import base64
import random
import string

from github import Github

def create_image(image_path, folder):
    encoded_image = image_path

    image_bytes = base64.b64decode(encoded_image)

    github_token = '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'
    g = Github(github_token)

    repo = g.get_user().get_repo('kartinki')

    file_name = generate_random_filename(16) + '.png'

    full_path = 'https://github.com/koiikf/kartinki/blob/main/' + folder + file_name

    repo.create_file(folder + file_name, 'Add file', image_bytes)

    return full_path

def generate_random_filename(length=16):
    characters = string.hexdigits + string.digits
    return ''.join(random.choice(characters) for _ in range(length))