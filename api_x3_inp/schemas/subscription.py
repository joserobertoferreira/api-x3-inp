from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


class SubscriptionAddressPublic(BaseModel):
    id: int
    customer: str
    address_code: str
    email_1: EmailStr | str
    email_2: EmailStr | str
    email_3: EmailStr | str
    email_4: EmailStr | str
    email_5: EmailStr | str
    created_at: datetime
    updated_at: datetime
    created_user: str
    updated_user: str
    model_config = ConfigDict(from_attributes=True)


class SubscriptionAddressList(BaseModel):
    addresses: list[SubscriptionAddressPublic]


class SubscriptionPublic(BaseModel):
    id: int
    number: str
    customer: str
    address_code: str
    model_config = ConfigDict(from_attributes=True)


class SubscriptionList(BaseModel):
    subscriptions: list[SubscriptionPublic]


class Subscriber(BaseModel):
    id: int
    customer: str
    name: str
    address_code: str | None = None
    company: str | None = None
    electronic_invoice: int
    model_config = ConfigDict(from_attributes=True)


class SubscriptionFullModel(BaseModel):
    number: str
    customer: str
    name: str
    address_code: str
    company: str
    electronic_invoice: int
    email_1: EmailStr | str
    email_2: EmailStr | str
    email_3: EmailStr | str
    email_4: EmailStr | str
    email_5: EmailStr | str


class SubscriptionFullList(BaseModel):
    subscriptions: list[SubscriptionFullModel]
