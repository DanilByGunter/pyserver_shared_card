from fastapi import status, APIRouter, Depends
from sqlalchemy import select, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.group_token.models import group_token, generate_token
from src.group_token.schemas import GroupTokenCreate, GroupTokenUpdate

import uuid
from datetime import datetime

router = APIRouter(
    prefix="/group_token",
    tags=["Group"]
)


# возвращает все токены
# @router.get('/', status_code=status.HTTP_200_OK)
# async def get_group_tokens(session: AsyncSession = Depends(get_async_session)):
#     query = select(group_token)
#     result = await session.execute(query)
#     return {'status': status.HTTP_200_OK, 'results': result.mappings().all()}


# возвращает токен по Id группы
@router.get('/{groupId}', status_code=status.HTTP_200_OK)
async def get_group_token(groupId: uuid.UUID, session: AsyncSession = Depends(get_async_session)):
    query = select(group_token).where(group_token.c.id == groupId)
    result = await session.execute(query)
    result = result.mappings().all()[0]
    diff = datetime.now() - result['date']
    if diff.total_seconds()/60 > 30:
        stmt = update(group_token).where(group_token.c.id == groupId).values(token=generate_token(), date=datetime.now())
        await session.execute(stmt)
        await session.commit()
        query = select(group_token).where(group_token.c.id == groupId)
        result = await session.execute(query)
        result = result.mappings().all()[0]
    return {'status': status.HTTP_200_OK, 'results': result}


# создаем токен
# @router.post('/', status_code=status.HTTP_201_CREATED)
# async def post_group_token(new_group_token: GroupTokenCreate, session: AsyncSession = Depends(get_async_session)):
#     stmt = insert(group_token).values(**new_group_token.dict())
#     await session.execute(stmt)
#     await session.commit()
#     return {"status": status.HTTP_201_CREATED}


# обновляем токен по Id группы
# @router.patch('/{groupId}', status_code=status.HTTP_200_OK)
# async def patch_group_token(groupId: uuid.UUID, session: AsyncSession = Depends(get_async_session)):
#     stmt = update(group_token).where(group_token.c.id_group == groupId).values(token=generate_token(), date=datetime.now())
#     await session.execute(stmt)
#     await session.commit()
#     return {"status": status.HTTP_200_OK}


# удаляем токен по Id группы
# @router.delete('/{group_tokenId}', status_code=status.HTTP_204_NO_CONTENT)
# async def delete_group_token(group_tokenId: uuid.UUID, session: AsyncSession = Depends(get_async_session)):
#     stmt = delete(group_token).where(group_token.c.id == group_tokenId)
#     await session.execute(stmt)
#     await session.commit()
#     return {"status": status.HTTP_204_NO_CONTENT}
