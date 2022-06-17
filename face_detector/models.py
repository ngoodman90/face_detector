import pydantic


class FaceRecognitionRequest(pydantic.BaseModel):
    image_url: str
