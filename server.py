import uvicorn
import fastapi
from fastapi.responses import RedirectResponse
from routers import Change
from routers import Contract
from routers import Customer
from routers import Materials
from routers import Orders
from routers import Price_list
from routers import Staff
from routers import Suppliers
from routers import Warehouse
from sql_base.base import BaseWorker

app = fastapi.FastAPI()
app.include_router(Change.router)
app.include_router(Contract.router)
app.include_router(Customer.router)
app.include_router(Materials.router)
app.include_router(Orders.router)
app.include_router(Price_list.router)
app.include_router(Staff.router)
app.include_router(Suppliers.router)
app.include_router(Warehouse.router)


if __name__ == '__main__':
    base_worker = BaseWorker()
    base_worker.set_base_path('sql_base/base.db')

    if not base_worker.check_base():
        base_worker.create_base('sql_base/scripts/3.sql')

    uvicorn.run("start_server:app", reload=True)