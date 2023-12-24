from fastapi import status, APIRouter, Depends
from sqlalchemy import select, insert, update, delete, join
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.recipe_product.models import product
from src.recipe.models import recipe
from src.metric.models import metric
from src.category.models import category
from src.recipe_product.models import recipe_product_association
from src.recipe_product.schemas import RecipeUpdate, RecipeCreate

router = APIRouter(
    prefix="/recipe_products",
    tags=["Recipe"]
)


# возвращает все сочетания
@router.get('/', status_code=status.HTTP_200_OK)
async def get_recipe_products(session: AsyncSession = Depends(get_async_session)):
    query = select(recipe_product_association)
    result = await session.execute(query)
    return {'status': status.HTTP_200_OK, 'results': result.mappings().all()}


# возвращает все рецепты с джойном
# @router.get('/joined', status_code=status.HTTP_200_OK)
# async def get_recipe_products(session: AsyncSession = Depends(get_async_session)):
#     query = select(recipe_product_association, product, recipe, metric).join(product).join(category).join(recipe).join(metric)
#     result = await session.execute(query)
#     return {'status': status.HTTP_200_OK, 'results': result.mappings().all()}


# возвращает рецепт по Id
# @router.get('/{recipeId}', status_code=status.HTTP_200_OK)
# async def get_recipe_product(recipeId: int, session: AsyncSession = Depends(get_async_session)):
#     query = select(recipe_product_association).where(recipe_product_association.c.id_recipe == recipeId)
#     result = await session.execute(query)
#     return {'status': status.HTTP_200_OK, 'results': result.mappings().all()}


# возвращает рецепт по Id джойном
# @router.get('/joined/{recipeId}', status_code=status.HTTP_200_OK)
# async def get_recipe_products(recipeId: int, session: AsyncSession = Depends(get_async_session)):
#     query = select(recipe_product_association, product, recipe, metric).join(product).join(category).join(recipe).join(metric).where(recipe_product_association.c.id_recipe == recipeId)
#     result = await session.execute(query)
#     return {'status': status.HTTP_200_OK, 'results': result.mappings().all()}


# создаем связку
# @router.post('/', status_code=status.HTTP_201_CREATED)
# async def post_recipe_product(new_recipe_product: RecipeCreate, session: AsyncSession = Depends(get_async_session)):
#     stmt = insert(recipe_product_association).values(**new_recipe_product.dict())
#     await session.execute(stmt)
#     await session.commit()
#     return {"status": status.HTTP_201_CREATED}


# обновляем рецепт по Id
# @router.patch('/{recipe_productId}', status_code=status.HTTP_200_OK)
# async def patch_recipe_product(recipe_productId: int, new_recipe_product: RecipeUpdate, session: AsyncSession = Depends(get_async_session)):
#     stmt = update(recipe_product_association).where(recipe_product_association.c.id == recipe_productId).values(**new_recipe_product.dict(exclude_unset=True))
#     await session.execute(stmt)
#     await session.commit()
#     return {"status": status.HTTP_200_OK}


# удаляем рецепт по Id
# @router.delete('/{recipe_product_Id}', status_code=status.HTTP_204_NO_CONTENT)
# async def delete_recipe_product(recipe_product_Id: int, session: AsyncSession = Depends(get_async_session)):
#     stmt = delete(recipe_product_association).where(recipe_product_association.c.id == recipe_product_Id)
#     await session.execute(stmt)
#     await session.commit()
#     return {"status": status.HTTP_204_NO_CONTENT}
