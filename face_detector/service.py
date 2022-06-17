import tempfile
from urllib import request

import face_recognition


def has_face(image_url: str) -> bool:
    with tempfile.NamedTemporaryFile() as image_file:
        request.urlretrieve(image_url, image_file.name)
        image_file.seek(0)
        image = face_recognition.load_image_file(image_file.name)
        return len(face_recognition.face_locations(image)) > 0
