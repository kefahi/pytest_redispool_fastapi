from redis.asyncio import ConnectionPool, Redis
from .settings import settings

REDIS_POOL : ConnectionPool = ConnectionPool(
        host=settings.redis_host,
        port=settings.redis_port,
        password=settings.redis_password,
        decode_responses=True,
        max_connections=settings.redis_pool_max,
    )

is_pytest : bool = False

class RedisService():
    async def __aenter__(self):
        if not hasattr(self, "_conn"):
            self._conn = await Redis(connection_pool=REDIS_POOL)
            if is_pytest:
                try:
                    await self._conn.ping()
                except RuntimeError:
                    pass
        return self

    async def __aexit__(self, exc_type, exc, tb):
        try:
            await self._conn.close()
        except:
            pass

    async def json_get(self,name: str) -> dict:
        return await self._conn.json().get(name=name)

    def pool_id(self):
        return id(self._conn.connection_pool)
