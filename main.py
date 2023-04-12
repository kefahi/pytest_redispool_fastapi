#!/usr/bin/env python3

from fastapi import FastAPI
from utils.redis_service import RedisService

import asyncio
from hypercorn.asyncio import serve
from hypercorn.config import Config

app = FastAPI()

@app.get("/one")
async def read_one():
    async with RedisService() as conn:
        spaces = await conn.json_get(name="spaces")
        print(conn.pool_id())
        return {"msg": "Hello One", "id": conn.pool_id(), "spaces": spaces}

@app.get("/two")
async def read_two():
    async with RedisService() as conn:
        spaces = await conn.json_get(name="spaces")
        print(conn.pool_id())
        return {"msg": "Hello Two", "id": conn.pool_id(), "spaces": spaces}

@app.get("/three")
async def read_three():
    async with RedisService() as conn:
        spaces = await conn.json_get(name="spaces")
        print(conn.pool_id())
        return {"msg": "Hello Three", "id": conn.pool_id(), "spaces": spaces}

if __name__ == "__main__":
    config: Config = Config()
    asyncio.run(serve(app, config))   # type: ignore
