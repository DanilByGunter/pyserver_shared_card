from fastapi import status, APIRouter, Depends
from sqlalchemy import select, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.category.models import category
from src.category.schemas import CategoryCreate, CategoryUpdate

router = APIRouter(
    prefix="/categories",
    tags=["Category"]
)


# возвращает все категории
@router.get('/', status_code=status.HTTP_200_OK)
async def get_categories(session: AsyncSession = Depends(get_async_session)):
    query = select(category)
    result = await session.execute(query)
    return {'status': status.HTTP_200_OK, 'results': result.mappings().all()}


# возвращает категорию по Id
# @router.get('/{categoryId}', status_code=status.HTTP_200_OK)
# async def get_category(categoryId: int, session: AsyncSession = Depends(get_async_session)):
#     query = select(category).where(category.c.id == categoryId)
#     result = await session.execute(query)
#     return {'status': status.HTTP_200_OK, 'results': result.mappings().all()}


# создаем категорию
# @router.post('/', status_code=status.HTTP_201_CREATED)
# async def post_category(new_category: CategoryCreate, session: AsyncSession = Depends(get_async_session)):
#     stmt = insert(category).values(**new_category.dict())
#     await session.execute(stmt)
#     await session.commit()
#     return {"status": status.HTTP_201_CREATED}


# обновляем категорию по Id
# @router.patch('/{categoryId}', status_code=status.HTTP_200_OK)
# async def patch_category(categoryId: int, new_category: CategoryUpdate, session: AsyncSession = Depends(get_async_session)):
#     stmt = update(category).where(category.c.id == categoryId).values(**new_category.dict(exclude_unset=True))
#     await session.execute(stmt)
#     await session.commit()
#     return {"status": status.HTTP_200_OK}


# удаляем категорию по Id
# @router.delete('/{categoryId}', status_code=status.HTTP_204_NO_CONTENT)
# async def delete_category(categoryId: int, session: AsyncSession = Depends(get_async_session)):
#     stmt = delete(category).where(category.c.id == categoryId)
#     await session.execute(stmt)
#     await session.commit()
#     return {"status": status.HTTP_204_NO_CONTENT}
