from fastapi import FastAPI
from src.category import routes as category_routes
from src.shop import routes as shop_routes
from src.currency import routes as currency_routes
from src.metric import routes as metric_routes
from src.user import routes as user_routes
from src.product import routes as product_routes
from src.recipe import routes as recipe_routes
from src.recipe_product import routes as recipe_product_routes
from src.group import routes as group_routes
from src.check import routes as check_routes
from src.group_user import routes as group_user_routes
from src.target import routes as target_routes
from src.group_token import routes as group_token_routes
from src.user_account.config import auth_backend, fastapi_users
from src.user_account.schemas import UserRead, UserCreate

app = FastAPI()

app.include_router(category_routes.router)
app.include_router(shop_routes.router)
app.include_router(currency_routes.router)
app.include_router(metric_routes.router)
app.include_router(user_routes.router)
app.include_router(product_routes.router)
app.include_router(recipe_routes.router)
app.include_router(recipe_product_routes.router)
app.include_router(group_routes.router)
app.include_router(check_routes.router)
app.include_router(group_user_routes.router)
app.include_router(target_routes.router)
app.include_router(group_token_routes.router)
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

@app.get("/api/healthchecker")
def root():
    return {"message": "Welcome to FastAPI with Pymongo"}