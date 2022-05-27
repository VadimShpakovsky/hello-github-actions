import pytest
from aiohttp.test_utils import TestClient

from server import init_app


@pytest.fixture
async def client(aiohttp_client) -> TestClient:
    app = init_app()
    return await aiohttp_client(app)


async def test_returns_hello(client: TestClient):
    response = await client.get("/hello")

    assert response.status == 200
    assert await response.text() == "Hello, world!"
