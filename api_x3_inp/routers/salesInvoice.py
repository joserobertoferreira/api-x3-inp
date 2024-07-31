from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from api_x3_inp.database.database import get_session
from api_x3_inp.models.salesInvoice import Invoice
from api_x3_inp.schemas.salesInvoice import SalesInvoiceList

router = APIRouter(prefix='/sales', tags=['sales'])

Session = Annotated[Session, Depends(get_session)]


@router.get('/invoice', response_model=SalesInvoiceList)
def read_sales_invoice(
    session: Session,  # type: ignore
    skip: int = 0,
    limit: int = 100,
):
    invoices = session.scalars(
        select(Invoice)
        .offset(skip)
        .limit(limit)
        .order_by(Invoice.account_date.desc(), Invoice.number.asc())
    )

    return {'invoices': invoices}
