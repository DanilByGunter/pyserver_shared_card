from fastapi import status, APIRouter, Depends
from sqlalchemy import select, insert, update, delete, join
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.product.models import product
from src.category.models import category
from src.product.schemas import ProductCreate, ProductUpdate

router = APIRouter(
    prefix="/products",
    tags=["Product"]
)


# возвращает все продукты
@router.get('/', status_code=status.HTTP_200_OK)
async def get_products(session: AsyncSession = Depends(get_async_session)):
    query = select(product)
    result = await session.execute(query)
    return {'status': status.HTTP_200_OK, 'results': result.all()}


# возвращает все продукты с джойном
@router.get('/joined', status_code=status.HTTP_200_OK)
async def get_products(session: AsyncSession = Depends(get_async_session)):
    query = select(product, category).join(category)
    result = await session.execute(query)
    return {'status': status.HTTP_200_OK, 'results': result.all()}


# возвращает продукт по Id
@router.get('/{productId}', status_code=status.HTTP_200_OK)
async def get_product(productId: int, session: AsyncSession = Depends(get_async_session)):
    query = select(product).where(product.c.id == productId)
    result = await session.execute(query)
    return {'status': status.HTTP_200_OK, 'results': result.all()}


# возвращает продукт по Id джойном
@router.get('/joined/{productId}', status_code=status.HTTP_200_OK)
async def get_products(productId: int, session: AsyncSession = Depends(get_async_session)):
    query = select(product, category).join(category).where(product.c.id == productId)
    result = await session.execute(query)
    return {'status': status.HTTP_200_OK, 'results': result.all()}


# создаем продукт
@router.post('/', status_code=status.HTTP_201_CREATED)
async def post_product(new_product: ProductCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(product).values(**new_product.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": status.HTTP_201_CREATED}


# обновляем продукт по Id
@router.patch('/{productId}', status_code=status.HTTP_200_OK)
async def patch_product(productId: int, new_product: ProductUpdate, session: AsyncSession = Depends(get_async_session)):
    stmt = update(product).where(product.c.id == productId).values(**new_product.dict(exclude_unset=True))
    await session.execute(stmt)
    await session.commit()
    return {"status": status.HTTP_200_OK}


# удаляем продукт по Id
@router.delete('/{productId}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(productId: int, session: AsyncSession = Depends(get_async_session)):
    stmt = delete(product).where(product.c.id == productId)
    await session.execute(stmt)
    await session.commit()
    return {"status": status.HTTP_204_NO_CONTENT}
