from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from api_x3_inp.database.database import get_session
from api_x3_inp.models.subscription import (
    Subscriber,
    Subscription,
    SubscriptionAddress,
)
from api_x3_inp.schemas.subscription import (
    SubscriptionAddressList,
    SubscriptionFullList,
)

router = APIRouter(prefix='/subscription', tags=['subscription'])

SubSession = Annotated[Session, Depends(get_session)]


@router.get('/address', response_model=SubscriptionAddressList)
def read_subscription_address(
    session: SubSession,
    skip: int = 0,
    limit: int = 100,
):
    addresses = session.scalars(
        select(SubscriptionAddress)
        .offset(skip)
        .limit(limit)
        .order_by(
            SubscriptionAddress.customer, SubscriptionAddress.address_code
        )
    )

    return {'addresses': addresses}


@router.get('/', response_model=SubscriptionFullList)
def read_subscriptions(session: SubSession, skip: int = 0, limit: int = 100):
    sim_flag = 2

    result = session.execute(
        select(
            Subscription.number,
            Subscription.customer,
            Subscription.address_code,
            Subscriber.name,
            Subscriber.company,
            Subscriber.electronic_invoice,
            SubscriptionAddress.email_1,
            SubscriptionAddress.email_2,
            SubscriptionAddress.email_3,
            SubscriptionAddress.email_4,
            SubscriptionAddress.email_5,
        )
        .select_from(Subscription)
        .join(
            Subscriber,
            Subscription.customer == Subscriber.customer,
        )
        .join(
            SubscriptionAddress,
            SubscriptionAddress.customer == Subscriber.customer,
        )
        .where(Subscriber.electronic_invoice == sim_flag)
        .offset(skip)
        .limit(limit)
        .order_by(Subscription.number)
    )

    subscriptions = []

    for row in result:
        subscription_full = {
            'number': row[0],
            'customer': row[1],
            'address_code': row[2],
            'name': row[3],
            'company': row[4],
            'electronic_invoice': row[5],
            'email_1': row[6],
            'email_2': row[7],
            'email_3': row[8],
            'email_4': row[9],
            'email_5': row[10],
        }

        subscriptions.append(subscription_full)

    return {'subscriptions': subscriptions}
