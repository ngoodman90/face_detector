import fastapi
import uvicorn
from face_detector.views import router as face_detector_router
from core.views import router as core_router

from config import settings

app = fastapi.FastAPI(
    title="Face Recognition",
    description="Face Recognition API",
    version="1.0.0",
    docs_url="/api/docs",
)


app.include_router(
    face_detector_router,
    prefix="/api/v1/faces",
    tags=["Face Detector"],
)


app.include_router(
    core_router,
    prefix="/api/v1",
    tags=["Core"],
)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG,
        access_log=False,
    )
