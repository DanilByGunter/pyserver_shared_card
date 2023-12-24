from fastapi import status, APIRouter, Depends
from sqlalchemy import select, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.target.models import target
from src.target.schemas import TargetCreate, TargetUpdate

import uuid

router = APIRouter(
    prefix="/targets",
    tags=["Target"]
)


# возвращает все цели
@router.get('/', status_code=status.HTTP_200_OK)
async def get_targets(session: AsyncSession = Depends(get_async_session)):
    query = select(target)
    result = await session.execute(query)
    return {'status': status.HTTP_200_OK, 'results': result.all()}


# возвращает цель по Id
@router.get('/{targetId}', status_code=status.HTTP_200_OK)
async def get_target_id(targetId: uuid.UUID, session: AsyncSession = Depends(get_async_session)):
    query = select(target).where(target.c.id == targetId)
    result = await session.execute(query)
    return {'status': status.HTTP_200_OK, 'results': result.all()}


# возвращает цель по Id группы
@router.get('/{groupId}', status_code=status.HTTP_200_OK)
async def get_target_groupid(groupId: uuid.UUID, session: AsyncSession = Depends(get_async_session)):
    query = select(target).where(target.c.id_group == groupId)
    result = await session.execute(query)
    return {'status': status.HTTP_200_OK, 'results': result.all()}


# создаем цель
@router.post('/', status_code=status.HTTP_201_CREATED)
async def post_target(new_target: TargetCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(target).values(**new_target.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": status.HTTP_201_CREATED}


# обновляем цель по Id
@router.patch('/{targetId}', status_code=status.HTTP_200_OK)
async def patch_target(targetId: uuid.UUID, new_target: TargetUpdate, session: AsyncSession = Depends(get_async_session)):
    stmt = update(target).where(target.c.id == targetId).values(**new_target.dict(exclude_unset=True))
    await session.execute(stmt)
    await session.commit()
    return {"status": status.HTTP_200_OK}


# удаляем цель по Id
@router.delete('/{targetId}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_target(targetId: uuid.UUID, session: AsyncSession = Depends(get_async_session)):
    stmt = delete(target).where(target.c.id == targetId)
    await session.execute(stmt)
    await session.commit()
    return {"status": status.HTTP_204_NO_CONTENT}
