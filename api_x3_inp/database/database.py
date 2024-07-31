from sqlalchemy import URL, create_engine
from sqlalchemy.orm import Session

from api_x3_inp.config.settings import Settings

url_object = URL.create(
    Settings().DB_DRIVER,
    username=Settings().DB_USERNAME,
    password=Settings().DB_PASSWORD,
    host=Settings().DB_SERVER,
    database=Settings().DB,
)

engine = create_engine(url_object, echo=True)


def get_session():  # pragma: no cover
    with Session(engine) as session:
        yield session
