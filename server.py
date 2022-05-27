from aiohttp import web


async def hello(_):
    return web.Response(text="Hello, world!")


def init_app() -> web.Application:
    app = web.Application()
    app.router.add_route('GET', '/hello', hello)

    return app


if __name__ == "__main__":
    app = init_app()
    web.run_app(app)
