from fastapi import APIRouter

from .endpoints.sample import router as sample_router


router = APIRouter()
router.include_router(sample_router)