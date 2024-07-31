from datetime import datetime

from sqlalchemy import (
    Date,
    DateTime,
    Integer,
    LargeBinary,
    Numeric,
    SmallInteger,
    String,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, registry

from api_x3_inp.config.settings import Settings

schema = Settings().DB_SCHEMA
table_registry = registry()


@table_registry.mapped_as_dataclass
class Subscription:
    """Tabela de assinaturas"""

    __tablename__ = 'ZSUBSCRIP'
    __table_args__ = {'schema': schema}

    id: Mapped[Numeric] = mapped_column(
        'ROWID', Numeric(38, 0), init=False, primary_key=True
    )
    upd_tick: Mapped[int] = mapped_column('UPDTICK_0', Integer, init=False)
    number: Mapped[str] = mapped_column(
        'SUBNUM_0', String(length=20), init=False, unique=True
    )
    subscription_type: Mapped[str] = mapped_column(
        'SUBTRS_0', String(length=20), init=False
    )
    customer: Mapped[str] = mapped_column(
        'SUBBPC_0', String(length=15), init=False
    )
    address_code: Mapped[str] = mapped_column(
        'SUBADD_0', String(length=5), init=False
    )
    subscription_date: Mapped[Date] = mapped_column(
        'SUBDAT_0', Date, init=False
    )
    pay_by_customer: Mapped[str] = mapped_column(
        'BPCPYR_0', String(length=15), init=False
    )
    payment_group: Mapped[str] = mapped_column(
        'GRPPYR_0', String(length=5), init=False
    )
    billing_type: Mapped[SmallInteger] = mapped_column(
        'INVFLG_0', SmallInteger, init=False
    )
    bill_editor: Mapped[SmallInteger] = mapped_column(
        'EDIINV_0', SmallInteger, init=False
    )
    payment_term: Mapped[str] = mapped_column(
        'PTE_0', String(length=15), init=False
    )
    invoice_number: Mapped[str] = mapped_column(
        'SIHNUM_0', String(length=20), init=False
    )
    editor: Mapped[str] = mapped_column(
        'EDINUM_0', String(length=20), init=False
    )
    bill_sales: Mapped[SmallInteger] = mapped_column(
        'SLSFLG_0', SmallInteger, init=False
    )
    start_term: Mapped[Date] = mapped_column('STREFF_0', Date, init=False)
    end_term: Mapped[Date] = mapped_column('ENDEFF_0', Date, init=False)
    suspended: Mapped[SmallInteger] = mapped_column(
        'BLKFLG_0', SmallInteger, init=False
    )
    start_suspension: Mapped[Date] = mapped_column(
        'STRINA_0', Date, init=False
    )
    end_suspension: Mapped[Date] = mapped_column('ENDINA_0', Date, init=False)
    quote_number: Mapped[str] = mapped_column(
        'SQHNUM_0', String(length=20), init=False
    )
    dimension_type: Mapped[str] = mapped_column(
        'DIE_0', String(length=3), init=False
    )
    analytical_dimension: Mapped[str] = mapped_column(
        'CCE_0', String(length=15), init=False
    )
    order_number: Mapped[str] = mapped_column(
        'SOHNUM_0', String(length=30), init=False
    )
    discount: Mapped[Numeric] = mapped_column(
        'DISCRGVAL_0', Numeric(10, 3), init=False
    )
    created_at: Mapped[datetime] = mapped_column(
        'CREDATTIM_0', DateTime, init=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        'UPDDATTIM_0', DateTime, init=False, server_onupdate=func.now()
    )
    created_user: Mapped[str] = mapped_column(
        'CREUSR_0', String(length=5), init=False
    )
    updated_user: Mapped[str] = mapped_column(
        'UPDUSR_0', String(length=5), init=False
    )
    uuid: Mapped[bytes] = mapped_column(
        'AUUID_0', LargeBinary(length=16), init=False
    )


"""     subscribers: Mapped[list['Subscriber']] = relationship(
        'Subscriber',
        primaryjoin='Subscriber.customer == Subscription.customer',
        foreign_keys=[customer],
        init=False,
        back_populates='subscription',
    )
 """


@table_registry.mapped_as_dataclass
class Subscriber:
    """Tabela de assinantes"""

    __tablename__ = 'ZSUBSCRIBER'
    __table_args__ = {'schema': schema}

    id: Mapped[Numeric] = mapped_column(
        'ROWID', Numeric(38, 0), init=False, primary_key=True
    )
    upd_tick: Mapped[int] = mapped_column('UPDTICK_0', Integer, init=False)
    customer: Mapped[str] = mapped_column(
        'SUBBPC_0', String(length=15), init=False, unique=True
    )
    name: Mapped[str] = mapped_column(
        'SUBNAM_0', String(length=70), init=False
    )
    address_code: Mapped[str] = mapped_column(
        'SUBADD_0', String(length=5), init=False
    )
    company: Mapped[str] = mapped_column(
        'SUBCPY_0', String(length=70), init=False
    )
    is_customer: Mapped[SmallInteger] = mapped_column(
        'BPCFLG_0', SmallInteger, init=False
    )
    payment_term: Mapped[str] = mapped_column(
        'PTE_0', String(length=15), init=False
    )
    tax_rule: Mapped[str] = mapped_column(
        'VACBPR_0', String(length=5), init=False
    )
    pay_by_customer: Mapped[str] = mapped_column(
        'BPCPYR_0', String(length=15), init=False
    )
    electronic_invoice: Mapped[SmallInteger] = mapped_column(
        'ELECTINV_0', SmallInteger, init=False
    )
    created_at: Mapped[datetime] = mapped_column(
        'CREDATTIM_0', DateTime, init=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        'UPDDATTIM_0', DateTime, init=False, server_onupdate=func.now()
    )
    created_user: Mapped[str] = mapped_column(
        'CREUSR_0', String(length=5), init=False
    )
    updated_user: Mapped[str] = mapped_column(
        'UPDUSR_0', String(length=5), init=False
    )
    uuid: Mapped[bytes] = mapped_column(
        'AUUID_0', LargeBinary(length=16), init=False
    )


"""     subscriptions: Mapped[list[Subscription]] = relationship(
        'Subscription',
        primaryjoin='Subscription.customer == Subscriber.customer',
        foreign_keys=[customer],
        init=False,
        back_populates='subscriber',
    )
 """


@table_registry.mapped_as_dataclass
class SubscriptionAddress:
    """Tabela de endereços das assinaturas"""

    __tablename__ = 'ZSUBSADDR'
    __table_args__ = {'schema': schema}

    id: Mapped[Numeric] = mapped_column(
        'ROWID', Numeric(38, 0), init=False, primary_key=True
    )
    upd_tick: Mapped[int] = mapped_column('UPDTICK_0', Integer, init=False)
    customer: Mapped[str] = mapped_column(
        'SUBBPC_0', String(length=15), init=False
    )
    address_code: Mapped[str] = mapped_column(
        'SUBADD_0', String(length=5), init=False
    )
    delivery_time: Mapped[SmallInteger] = mapped_column(
        'DAYLTI_0', SmallInteger, init=False
    )
    zone: Mapped[str] = mapped_column('ZONA_0', String(length=20), init=False)
    sub_zone: Mapped[str] = mapped_column(
        'SUBZONA_0', String(length=20), init=False
    )
    structure: Mapped[str] = mapped_column(
        'STRUNUM_0', String(length=20), init=False
    )
    route: Mapped[str] = mapped_column('ROTA_0', String(length=20), init=False)
    doc_type: Mapped[SmallInteger] = mapped_column(
        'DOCTYP_0', SmallInteger, init=False
    )
    delivery_mode: Mapped[str] = mapped_column(
        'MDL_0', String(length=5), init=False
    )
    charge_type: Mapped[str] = mapped_column(
        'COLTYP_0', String(length=20), init=False
    )
    email_1: Mapped[str] = mapped_column(
        'EMAIL_0', String(length=100), init=False
    )
    email_2: Mapped[str] = mapped_column(
        'EMAIL_1', String(length=100), init=False
    )
    email_3: Mapped[str] = mapped_column(
        'EMAIL_2', String(length=100), init=False
    )
    email_4: Mapped[str] = mapped_column(
        'EMAIL_3', String(length=100), init=False
    )
    email_5: Mapped[str] = mapped_column(
        'EMAIL_4', String(length=100), init=False
    )
    created_at: Mapped[datetime] = mapped_column(
        'CREDATTIM_0', DateTime, init=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        'UPDDATTIM_0', DateTime, init=False, server_onupdate=func.now()
    )
    created_user: Mapped[str] = mapped_column(
        'CREUSR_0', String(length=5), init=False
    )
    updated_user: Mapped[str] = mapped_column(
        'UPDUSR_0', String(length=5), init=False
    )
    uuid: Mapped[bytes] = mapped_column(
        'AUUID_0', LargeBinary(length=16), init=False
    )
