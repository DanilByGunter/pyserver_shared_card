from fastapi import status, APIRouter, Depends
from sqlalchemy import select, insert, update, delete, join
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.check.models import check
from src.product.models import product
from src.metric.models import metric
from src.user.models import user
from src.shop.models import shop
from src.currency.models import currency
from src.group.models import group
from src.category.models import category
from src.check.schemas import CheckCreate, CheckUpdate

import uuid

router = APIRouter(
    prefix="/checks",
    tags=["Check"]
)


# возвращает все чеки
@router.get('/', status_code=status.HTTP_200_OK)
async def get_checks(session: AsyncSession = Depends(get_async_session)):
    query = select(check)
    result = await session.execute(query)
    return {'status': status.HTTP_200_OK, 'results': result.all()}


# # возвращает все чеки с джойном
# @router.get('/joined', status_code=status.HTTP_200_OK)
# async def get_checks_join(session: AsyncSession = Depends(get_async_session)):
#     query = select(check, category).join(category)
#     result = await session.execute(query)
#     return {'status': status.HTTP_200_OK, 'results': result.all()}


# возвращает чек по Id
@router.get('/{checkId}', status_code=status.HTTP_200_OK)
async def get_check_id(checkId: uuid.UUID, session: AsyncSession = Depends(get_async_session)):
    query = select(check).where(check.c.id == checkId)
    result = await session.execute(query)
    return {'status': status.HTTP_200_OK, 'results': result.all()}


# возвращает чек по Id
@router.get('/{groupId}', status_code=status.HTTP_200_OK)
async def get_check_groupid(groupId: uuid.UUID, session: AsyncSession = Depends(get_async_session)):
    query = select(check).where(check.c.id_group == groupId)
    result = await session.execute(query)
    return {'status': status.HTTP_200_OK, 'results': result.all()}


# # возвращает чек по Id джойном
# @router.get('/joined/{checkId}', status_code=status.HTTP_200_OK)
# async def get_check_join(checkId: uuid.UUID, session: AsyncSession = Depends(get_async_session)):
#     query = select(check, product, shop).join(product).join(shop).where(check.c.id == checkId)
#     result = await session.execute(query)
#     return {'status': status.HTTP_200_OK, 'results': result.all()}


# # возвращает чек по groupId джойном
# @router.get('/joined/{groupId}', status_code=status.HTTP_200_OK)
# async def get_check_join(groupId: uuid.UUID, session: AsyncSession = Depends(get_async_session)):
#     query = select(check, product, metric, user.c.name, shop.c.name, currency.c.name, group.c.name)\
#         .join(product).join(metric).join(user).join(shop).join(currency).join(group)\
#         .where(check.c.id_group == groupId)
#     result = await session.execute(query)
#     return {'status': status.HTTP_200_OK, 'results': result.all()}


# создаем чек
@router.post('/', status_code=status.HTTP_201_CREATED)
async def post_check(new_check: CheckCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(check).values(**new_check.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": status.HTTP_201_CREATED}


# обновляем чек по Id
@router.patch('/{checkId}', status_code=status.HTTP_200_OK)
async def patch_check(checkId: uuid.UUID, new_check: CheckUpdate, session: AsyncSession = Depends(get_async_session)):
    stmt = update(check).where(check.c.id == checkId).values(**new_check.dict(exclude_unset=True))
    await session.execute(stmt)
    await session.commit()
    return {"status": status.HTTP_200_OK}


# удаляем чек по Id
@router.delete('/{checkId}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_check(checkId: uuid.UUID, session: AsyncSession = Depends(get_async_session)):
    stmt = delete(check).where(check.c.id == checkId)
    await session.execute(stmt)
    await session.commit()
    return {"status": status.HTTP_204_NO_CONTENT}
