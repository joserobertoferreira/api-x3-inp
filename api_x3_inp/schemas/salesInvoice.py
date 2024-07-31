from datetime import date

from pydantic import BaseModel, ConfigDict


class SalesInvoicePublic(BaseModel):
    id: int
    number: str
    invoice_type: str
    invoice_category: int
    company: str
    customer: str
    account_date: date
    currency: str
    currency_local: str
    full_name: str
    country: str
    country_name: str
    amount: float
    amount_local: float
    model_config = ConfigDict(from_attributes=True)


class SalesInvoiceList(BaseModel):
    invoices: list[SalesInvoicePublic]
