from fastapi import FastAPI, HTTPException
from starlette.status import HTTP_403_FORBIDDEN
from pydantic import BaseModel
from . import db


class RequestBody(BaseModel):
    log_data: dict
    user_token: str


api = FastAPI()


@api.post("/logs")
def add_log(body: RequestBody):
    user = db.get_user_by_token(body.user_token)
    if not user:
        raise HTTPException(status_code=HTTP_403_FORBIDDEN)
    db.add_log(body.user_token, body.log_data)
    return {"result": "ok", "log_data": body.log_data}
