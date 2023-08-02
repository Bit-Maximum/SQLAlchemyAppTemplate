from starlette.responses import JSONResponse
import typing


class CustomResponse(JSONResponse):
    def render(self, content: typing.Any) -> bytes:
        return super(CustomResponse, self).render({
            "data": content,
            "version": "1.0.0"
        })
