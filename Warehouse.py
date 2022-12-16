from fastapi import APIRouter
from sql_base.models import Warehouse
import resolvers.warehouse

warehouse = APIRouter()


@warehouse.get('/')
def get_warehouse():
    return f'Response: {{text: Страница со списком склада }}'


@warehouse.post('/')
def new_warehouse(warehouse: Warehouse,):
    new_id = resolvers.warehouse.new_warehouse(warehouse)
    return f'{{code: 201, id: {new_id}}}'


@warehouse.get(f'/{warehouse_id}')
def get_warehouse(warehouse_id: int):
    warehouse = resolvers.get_warehouse(warehouse_id)
    return 'warehouse: {n_warehouse: название склада , address: адрес , name_of_the_material: название материалов , remains: остаток , supplier: поставщики ,}'


@warehouse.put(f'/{warehouse_id}')
def update_warehouse(warehouse_id: int):
     return f'Update orders {warehouse_id}'


@warehouse.delete(f'/{warehouse_id}')
def delelte_warehouse(warehouse_id: int):
     return f'delete orders {warehouse_id}'