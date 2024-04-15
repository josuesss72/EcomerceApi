from starlette.status import *
from fastapi.responses import JSONResponse
from typing import Union
from interfaces.user_interface import IUser
from interfaces.product_interface import IProduct


class responsesHttp:

    def __init__(
        self, entity: Union[IUser, list[IUser], IProduct, list[IProduct], str]
    ):
        self.HTTP_401 = JSONResponse(
            status_code=HTTP_401_UNAUTHORIZED,
            content={"message": "Error", "content": f"{entity} not authorized"},
        )
        self.HTTP_404 = JSONResponse(
            status_code=HTTP_404_NOT_FOUND,
            content={"message": "Error", "content": f"{entity} not found"},
        )
        self.HTTP_200 = JSONResponse(
            status_code=HTTP_200_OK,
            content={"message": "success", "content": entity},
        )
        self.HTTP_201 = JSONResponse(
            status_code=HTTP_201_CREATED,
            content={"message": "success", "content": entity},
        )
        self.HTTP_202 = JSONResponse(
            status_code=HTTP_202_ACCEPTED,
            content={
                "message": "success",
                "content": f"{entity} deleted correctly",
            },
        )
        self.HTTP_409 = JSONResponse(
            status_code=HTTP_409_CONFLICT,
            content={
                "message": "Error",
                "content": f"{entity} is exists in database",
            },
        )
