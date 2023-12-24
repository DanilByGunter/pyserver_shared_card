from fastapi import status, APIRouter, Depends
from sqlalchemy import select, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.recipe.models import recipe
from src.recipe.schemas import RecipeCreate, RecipeUpdate

router = APIRouter(
    prefix="/recipes",
    tags=["Recipe"]
)


# возвращает все рецепты
@router.get('/', status_code=status.HTTP_200_OK)
async def get_recipes(session: AsyncSession = Depends(get_async_session)):
    query = select(recipe)
    result = await session.execute(query)
    return {'status': status.HTTP_200_OK, 'results': result.all()}


# возвращает рецепт по Id
@router.get('/{recipeId}', status_code=status.HTTP_200_OK)
async def get_recipe(recipeId: int, session: AsyncSession = Depends(get_async_session)):
    query = select(recipe).where(recipe.c.id == recipeId)
    result = await session.execute(query)
    return {'status': status.HTTP_200_OK, 'results': result.all()}


# создаем рецепт
@router.post('/', status_code=status.HTTP_201_CREATED)
async def post_recipe(new_recipe: RecipeCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(recipe).values(**new_recipe.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": status.HTTP_201_CREATED}


# обновляем рецепт по Id
@router.patch('/{recipeId}', status_code=status.HTTP_200_OK)
async def patch_recipe(recipeId: int, new_recipe: RecipeUpdate, session: AsyncSession = Depends(get_async_session)):
    stmt = update(recipe).where(recipe.c.id == recipeId).values(**new_recipe.dict(exclude_unset=True))
    await session.execute(stmt)
    await session.commit()
    return {"status": status.HTTP_200_OK}


# удаляем рецепт по Id
@router.delete('/{recipeId}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_recipe(recipeId: int, session: AsyncSession = Depends(get_async_session)):
    stmt = delete(recipe).where(recipe.c.id == recipeId)
    await session.execute(stmt)
    await session.commit()
    return {"status": status.HTTP_204_NO_CONTENT}
