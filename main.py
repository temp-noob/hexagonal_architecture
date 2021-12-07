import os
import typing
from repository_adapters.db_impl import psql_adapter, csql_adapter
from src.repositories.repository import Repository

DB: typing.Optional[Repository] = None

if os.environ["CURRENT_DB"] == "PSQL":
    DB = psql_adapter.PsqlAdapter()
elif os.environ["CURRENT_DB"] == "CSQL":
    DB = csql_adapter.CsqlAdapter()

if os.environ["TRANSFER_LAYER"] == "REST":
    os.system('cd transport_layer && flask run')

elif os.environ["TRANSFER_LAYER"] == "GQL":
    os.system('cd transport_layer && strawberry server schema')
    pass
