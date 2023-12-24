from fastapi_users.authentication import CookieTransport, JWTStrategy, AuthenticationBackend
from fastapi_users import FastAPIUsers

from src.user_account.manager import get_user_manager
from src.user_account.models import UserAccount
from src.config import SECRET_AUTH

from uuid import UUID

cookie_transport = CookieTransport(cookie_name='default', cookie_max_age=3600)

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET_AUTH, lifetime_seconds=3600)

auth_backend = AuthenticationBackend(
    name='jwt',
    transport=cookie_transport,
    get_strategy=get_jwt_strategy
)

fastapi_users = FastAPIUsers[UserAccount, UUID](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user()