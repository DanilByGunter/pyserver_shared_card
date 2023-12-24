from fastapi import status, APIRouter, Depends
from sqlalchemy import select, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.currency.models import currency
from src.currency.schemas import CurrencyCreate, CurrencyUpdate

router = APIRouter(
    prefix="/currencys",
    tags=["Currency"]
)


# возвращает все валюты
@router.get('/', status_code=status.HTTP_200_OK)
async def get_currencys(session: AsyncSession = Depends(get_async_session)):
    query = select(currency)
    result = await session.execute(query)
    return result.mappings().all()


# возвращает валюту по Id
# @router.get('/{code}', status_code=status.HTTP_200_OK)
# async def get_currency(code: str, session: AsyncSession = Depends(get_async_session)):
#     query = select(currency).where(currency.c.code == code)
#     result = await session.execute(query)
#     return {'status': status.HTTP_200_OK, 'results': result.mappings().all()}


# создаем валюту
# @router.post('/', status_code=status.HTTP_201_CREATED)
# async def post_currency(new_currency: CurrencyCreate, session: AsyncSession = Depends(get_async_session)):
#     stmt = insert(currency).values(**new_currency.dict())
#     await session.execute(stmt)
#     await session.commit()
#     return {"status": status.HTTP_201_CREATED}


# обновляем валюту по Id
# @router.patch('/{code}', status_code=status.HTTP_200_OK)
# async def patch_currency(code: str, new_currency: CurrencyUpdate, session: AsyncSession = Depends(get_async_session)):
#     stmt = update(currency).where(currency.c.id == code).values(**new_currency.dict(exclude_unset=True))
#     await session.execute(stmt)
#     await session.commit()
#     return {"status": status.HTTP_200_OK}


# удаляем валюту по Id
# @router.delete('/{code}', status_code=status.HTTP_204_NO_CONTENT)
# async def delete_currency(code: str, session: AsyncSession = Depends(get_async_session)):
#     stmt = delete(currency).where(currency.c.id == code)
#     await session.execute(stmt)
#     await session.commit()
#     return {"status": status.HTTP_204_NO_CONTENT}
