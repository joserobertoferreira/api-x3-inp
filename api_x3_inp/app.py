from http import HTTPStatus

from fastapi import FastAPI

from api_x3_inp.routers import salesInvoice, subscription
from api_x3_inp.schemas.schemas import Message

app = FastAPI()

app.include_router(subscription.router)
app.include_router(salesInvoice.router)


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Hello World!'}
