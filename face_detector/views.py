import fastapi

from face_detector import models, service

router = fastapi.APIRouter()


@router.post("")
def has_face(request_body: models.FaceRecognitionRequest) -> bool:
    return service.has_face(request_body.image_url)
