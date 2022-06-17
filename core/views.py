import fastapi

router = fastapi.APIRouter()


@router.get("/health")
async def health() -> dict:
    return {"status": "ok"}
