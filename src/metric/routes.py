from fastapi import status, APIRouter, Depends
from sqlalchemy import select, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.metric.models import metric
from src.metric.schemas import MetricCreate, MetricUpdate

router = APIRouter(
    prefix="/metrics",
    tags=["Metric"]
)


# возвращает все метрики
@router.get('/', status_code=status.HTTP_200_OK)
async def get_metrics(session: AsyncSession = Depends(get_async_session)):
    query = select(metric)
    result = await session.execute(query)
    return {'status': status.HTTP_200_OK, 'results': result.all()}


# возвращает метрику по Id
@router.get('/{metricId}', status_code=status.HTTP_200_OK)
async def get_metric(metricId: int, session: AsyncSession = Depends(get_async_session)):
    query = select(metric).where(metric.c.id == metricId)
    result = await session.execute(query)
    return {'status': status.HTTP_200_OK, 'results': result.all()}


# создаем метрику
@router.post('/', status_code=status.HTTP_201_CREATED)
async def post_metric(new_metric: MetricCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(metric).values(**new_metric.dict())
    print(stmt)
    await session.execute(stmt)
    await session.commit()
    return {"status": status.HTTP_201_CREATED}


# обновляем метрику по Id
@router.patch('/{metricId}', status_code=status.HTTP_200_OK)
async def patch_metric(metricId: int, new_metric: MetricUpdate, session: AsyncSession = Depends(get_async_session)):
    stmt = update(metric).where(metric.c.id == metricId).values(**new_metric.dict(exclude_unset=True))
    await session.execute(stmt)
    await session.commit()
    return {"status": status.HTTP_200_OK}


# удаляем метрику по Id
@router.delete('/{metricId}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_metric(metricId: int, session: AsyncSession = Depends(get_async_session)):
    stmt = delete(metric).where(metric.c.id == metricId)
    await session.execute(stmt)
    await session.commit()
    return {"status": status.HTTP_204_NO_CONTENT}
