from fastapi import status, APIRouter, Depends
from sqlalchemy import select, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.user.models import user
from src.user_account.models import user_account
from src.user.schemas import UserCreate, UserUpdate

import uuid

router = APIRouter(
    prefix="/users",
    tags=["User"]
)


# возвращает всех пользователей
# @router.get('/', status_code=status.HTTP_200_OK)
# async def get_users(session: AsyncSession = Depends(get_async_session)):
#     query = select(user)
#     result = await session.execute(query)
#     return {'status': status.HTTP_200_OK, 'results': result.mappings().all()}


# возвращает пользователя по Id
@router.get('/{userId}', status_code=status.HTTP_200_OK)
async def get_user(userId: uuid.UUID, session: AsyncSession = Depends(get_async_session)):
    query = select(user).where(user.c.id == userId)
    result = await session.execute(query)
    return {'status': status.HTTP_200_OK, 'results': result.mappings().all()}


# создаем пользователя
@router.post('/', status_code=status.HTTP_201_CREATED)
async def post_user(new_user: UserCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(user).values(**new_user.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": status.HTTP_201_CREATED}


# обновляем пользователя по Id
@router.patch('/{userId}', status_code=status.HTTP_200_OK)
async def patch_user(userId: uuid.UUID, new_user: UserUpdate, session: AsyncSession = Depends(get_async_session)):
    stmt = update(user).where(user.c.id == userId).values(**new_user.dict(exclude_unset=True))
    await session.execute(stmt)
    await session.commit()
    return {"status": status.HTTP_200_OK}


# удаляем пользователя по Id
@router.delete('/{userId}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(userId: uuid.UUID, session: AsyncSession = Depends(get_async_session)):
    stmt = delete(user).where(user.c.id == userId)
    await session.execute(stmt)
    await session.commit()
    return {"status": status.HTTP_204_NO_CONTENT}
