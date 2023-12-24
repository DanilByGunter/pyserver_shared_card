from fastapi import status, APIRouter, Depends
from sqlalchemy import select, insert, update, delete, join
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.user.models import user
from src.group.models import group
from src.group_user.models import group_user_association
from src.group_user.schemas import GroupUpdate, GroupCreate

import uuid

router = APIRouter(
    prefix="/group_users",
    tags=["Group"]
)


# возвращает все сочетания
# @router.get('/', status_code=status.HTTP_200_OK)
# async def get_group_users(session: AsyncSession = Depends(get_async_session)):
#     query = select(group_user_association)
#     result = await session.execute(query)
#     return {'status': status.HTTP_200_OK, 'results': result.mappings().all()}


# возвращает все группы с джойном
# @router.get('/joined', status_code=status.HTTP_200_OK)
# async def get_group_users(session: AsyncSession = Depends(get_async_session)):
#     query = select(group_user_association, group, user).join(group).join(user)
#     result = await session.execute(query)
#     return {'status': status.HTTP_200_OK, 'results': result.mappings().all()}


# возвращает группу по Id группы
@router.get('/{groupId}', status_code=status.HTTP_200_OK)
async def get_group_user(groupId: uuid.UUID, session: AsyncSession = Depends(get_async_session)):
    query = select(group_user_association).where(group_user_association.c.id_group == groupId)
    result = await session.execute(query)
    return {'status': status.HTTP_200_OK, 'results': result.mappings().all()}


# возвращает группу по Id джойном
# @router.get('/joined/{groupId}', status_code=status.HTTP_200_OK)
# async def get_group_users(groupId: uuid.UUID, session: AsyncSession = Depends(get_async_session)):
#     query = select(group_user_association, group, user).join(group).join(user).where(group_user_association.c.id_group == groupId)
#     result = await session.execute(query)
#     return {'status': status.HTTP_200_OK, 'results': result.mappings().all()}


# создаем связку
@router.post('/', status_code=status.HTTP_201_CREATED)
async def post_group_user(new_group_user: GroupCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(group_user_association).values(**new_group_user.dict())
    print(new_group_user.dict())
    print(stmt)
    await session.execute(stmt)
    await session.commit()
    return {"status": status.HTTP_201_CREATED}


# обновляем группу по Id
@router.patch('/{groupId}', status_code=status.HTTP_200_OK)
async def patch_group_user(groupId: uuid.UUID, new_group_user: GroupUpdate, session: AsyncSession = Depends(get_async_session)):
    stmt = update(group_user_association).where(group_user_association.c.id_group == groupId).values(**new_group_user.dict(exclude_unset=True))
    await session.execute(stmt)
    await session.commit()
    return {"status": status.HTTP_200_OK}


# удаляем пользователя из группы по Id
@router.delete('/{userId}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_group_user(userId: uuid.UUID, session: AsyncSession = Depends(get_async_session)):
    stmt = delete(group_user_association).where(group_user_association.c.id_user == userId)
    await session.execute(stmt)
    await session.commit()
    return {"status": status.HTTP_204_NO_CONTENT}
