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
class Invoice:
    """Tabela SINVOICE - Faturas venda"""

    __tablename__ = 'SINVOICE'
    __table_args__ = {'schema': schema}

    id: Mapped[Numeric] = mapped_column(
        'ROWID', Numeric(38, 0), init=False, primary_key=True
    )
    upd_tick: Mapped[int] = mapped_column('UPDTICK_0', Integer, init=False)
    number: Mapped[str] = mapped_column(
        'NUM_0', String(length=20), init=False, unique=True
    )
    invoice_type: Mapped[str] = mapped_column(
        'SIVTYP_0', String(length=5), init=False
    )
    invoice_category: Mapped[SmallInteger] = mapped_column(
        'INVTYP_0', SmallInteger, init=False
    )
    company: Mapped[str] = mapped_column('CPY_0', String(length=5), init=False)
    customer: Mapped[str] = mapped_column(
        'BPR_0', String(length=15), init=False
    )
    account_date: Mapped[Date] = mapped_column('ACCDAT_0', Date, init=False)
    currency: Mapped[String] = mapped_column(
        'CUR_0', String(length=3), init=False
    )
    currency_local: Mapped[String] = mapped_column(
        'CURLED_0', String(length=3), init=False
    )
    name: Mapped[String] = mapped_column(
        'BPRNAM_0', String(length=35), init=False
    )
    name1: Mapped[String] = mapped_column(
        'BPRNAM_1', String(length=35), init=False
    )
    country: Mapped[str] = mapped_column('CRY_0', String(length=3), init=False)
    country_name: Mapped[str] = mapped_column(
        'CRYNAM_0', String(length=40), init=False
    )
    amount: Mapped[Numeric] = mapped_column(
        'AMTATI_0', Numeric(27, 13), init=False
    )
    amount_local: Mapped[Numeric] = mapped_column(
        'AMTATIL_0', Numeric(27, 13), init=False
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

    @property
    def full_name(self):
        return f'{self.name} {self.name1}'


@table_registry.mapped_as_dataclass
class InvoiceValorization:
    """Tabela SINVOICEV - Fatura venda valorização"""

    __tablename__ = 'SINVOICEV'
    __table_args__ = {'schema': schema}

    id: Mapped[Numeric] = mapped_column(
        'ROWID', Numeric(38, 0), init=False, primary_key=True
    )
    upd_tick: Mapped[int] = mapped_column('UPDTICK_0', Integer, init=False)
    number: Mapped[str] = mapped_column(
        'NUM_0', String(length=20), init=False, unique=True
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


@table_registry.mapped_as_dataclass
class InvoiceDetail:
    """Tabela SINVOICED - Det. fatura de venda"""

    __tablename__ = 'SINVOICED'
    __table_args__ = {'schema': schema}

    id: Mapped[Numeric] = mapped_column(
        'ROWID', Numeric(38, 0), init=False, primary_key=True
    )
    upd_tick: Mapped[int] = mapped_column('UPDTICK_0', Integer, init=False)
    number: Mapped[str] = mapped_column(
        'NUM_0', String(length=20), init=False, unique=True
    )
    line: Mapped[Integer] = mapped_column('SIDLIN_0', Integer, init=False)
    product: Mapped[str] = mapped_column(
        'ITMREF_0', String(length=20), init=False
    )
    description: Mapped[str] = mapped_column(
        'ZITMDES_0', String(length=100), init=False
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
