import fastapi
import uvicorn

from containers import Container
from users.api import router as users_router
from appresponse import CustomResponse


app = fastapi.FastAPI(default_response_class=CustomResponse)
app.include_router(users_router, prefix="/users")

container = Container()


if __name__ == "__main__":
    uvicorn.run(app)
    