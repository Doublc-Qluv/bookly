from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession

from src.db.models import User, Review
from src.db.main import get_session
from src.auth.dependencies import get_current_user
from .schemas import ReviewCreateModel
from .service import ReviewService



review_service = ReviewService()
review_router = APIRouter()


@review_router.post("/book/{book_uid}")
async def add_review_to_books(
    book_uid: str,
    review_data: ReviewCreateModel,
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_session),
):
    new_review = await review_service.add_review_to_book(
        user_email=current_user.email,
        book_uid=book_uid,
        review_data=review_data,
        session=session,
    )
    return new_review
