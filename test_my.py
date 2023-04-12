# from conftest import get_test_redis_pool  # pyright: ignore
import utils.redis_service

utils.redis_service.is_pytest = True

from fastapi.testclient import TestClient
import asyncio
from main import app

client = TestClient(app)

async def test_read_one():
    response = client.get("/one")
    assert response.status_code == 200
    json = response.json()
    assert json["msg"] == "Hello One"
    # print(json["spaces"]["management"])

async def test_read_two():
    response = client.get("/two")
    assert response.status_code == 200
    json = response.json()
    assert json["msg"] == "Hello Two"
    # print(json["spaces"]["management"])

async def test_read_three():
    response = client.get("/three")
    assert response.status_code == 200
    json = response.json()
    assert json["msg"] == "Hello Three"
    # print(json["spaces"]["management"])


async def main():
    await test_read_one()
    await asyncio.sleep(1)
    await test_read_two()
    await asyncio.sleep(1)
    await test_read_three()

if __name__ == "__main__":
    print("Good evening ...")
    # asyncio.get_event_loop().run_until_complete(main())
    asyncio.run(main())

