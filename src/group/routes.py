from fastapi import status, APIRouter, Depends
from sqlalchemy import select, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.group.models import group
from src.group_token.models import group_token

from src.group.schemas import GroupCreate, GroupUpdate

import uuid

router = APIRouter(
    prefix="/groups",
    tags=["Group"]
)


# возвращает все группы
# @router.get('/', status_code=status.HTTP_200_OK)
# async def get_groups(session: AsyncSession = Depends(get_async_session)):
#     query = select(group)
#     result = await session.execute(query)
#     return {'status': status.HTTP_200_OK, 'results': result.mappings().all()}


# возвращает группу по Id
@router.get('/{groupId}', status_code=status.HTTP_200_OK)
async def get_group(groupId: uuid.UUID, session: AsyncSession = Depends(get_async_session)):
    query = select(group).where(group.c.id == groupId)
    result = await session.execute(query)
    result = result.mappings().all()[0]
    return {'status': status.HTTP_200_OK, 'results': result}


# создаем группу
@router.post('/', status_code=status.HTTP_201_CREATED)
async def post_group(new_group: GroupCreate, session: AsyncSession = Depends(get_async_session)):
    query = insert(group).values(**new_group.dict()).returning(group.c.id)
    result = await session.execute(query)
    result = result.mappings().all()[0]
    
    query = insert(group_token).values(**result)
    await session.execute(query)
    await session.commit()
    
    return {"status": status.HTTP_201_CREATED, 'results': result}


# обновляем группу по Id
@router.patch('/{groupId}', status_code=status.HTTP_200_OK)
async def patch_group(groupId: uuid.UUID, new_group: GroupUpdate, session: AsyncSession = Depends(get_async_session)):
    stmt = update(group).where(group.c.id == groupId).values(**new_group.dict(exclude_unset=True))
    await session.execute(stmt)
    await session.commit()
    return {"status": status.HTTP_200_OK}


# удаляем группу по Id
@router.delete('/{groupId}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_group(groupId: uuid.UUID, session: AsyncSession = Depends(get_async_session)):
    stmt = delete(group).where(group.c.id == groupId)
    await session.execute(stmt)
    await session.commit()
    return {"status": status.HTTP_204_NO_CONTENT}
