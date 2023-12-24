from fastapi import status, APIRouter, Depends
from sqlalchemy import select, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.shop.models import shop
from src.shop.schemas import ShopCreate, ShopUpdate

router = APIRouter(
    prefix="/shops",
    tags=["Shop"]
)


# возвращает все магазины
@router.get('/', status_code=status.HTTP_200_OK)
async def get_shops(session: AsyncSession = Depends(get_async_session)):
    query = select(shop)
    result = await session.execute(query)
    return {'status': status.HTTP_200_OK, 'results': result.all()}


# возвращает магазин по Id
@router.get('/{shopId}', status_code=status.HTTP_200_OK)
async def get_shop(shopId: int, session: AsyncSession = Depends(get_async_session)):
    query = select(shop).where(shop.c.id == shopId)
    result = await session.execute(query)
    return {'status': status.HTTP_200_OK, 'results': result.all()}


# создаем магазин
@router.post('/', status_code=status.HTTP_201_CREATED)
async def post_shop(new_shop: ShopCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(shop).values(**new_shop.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": status.HTTP_201_CREATED}


# обновляем магазин по Id
@router.patch('/{shopId}', status_code=status.HTTP_200_OK)
async def patch_shop(shopId: int, new_shop: ShopUpdate, session: AsyncSession = Depends(get_async_session)):
    stmt = update(shop).where(shop.c.id == shopId).values(**new_shop.dict(exclude_unset=True))
    await session.execute(stmt)
    await session.commit()
    return {"status": status.HTTP_200_OK}


# удаляем магазин по Id
@router.delete('/{shopId}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_shop(shopId: int, session: AsyncSession = Depends(get_async_session)):
    stmt = delete(shop).where(shop.c.id == shopId)
    await session.execute(stmt)
    await session.commit()
    return {"status": status.HTTP_204_NO_CONTENT}
