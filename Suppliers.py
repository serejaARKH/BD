from fastapi import APIRouter
from sql_base.models import Suppliers
import resolvers.suppliers

suppliers = APIRouter()


@suppliers.get('/')
def get_suppliers():
    return f'Response: {{text: Страница со списком поставщиков }}'


@suppliers.post('/')
def new_suppliers(suppliers: Suppliers,):
    new_id = resolvers.suppliers.new_suppliers(suppliers)
    return f'{{code: 201, id: {new_id}}}'


@suppliers.get(f'/{suppliers_id}')
def get_suppliers(suppliers_id: int):
    suppliers = resolvers.get_suppliers(suppliers_id)
    return 'suppliers: {name_of_the_organization: название организации, address: адрес}'


@suppliers.put(f'/{supplierss_id}')
def update_suppliers(supplie_id: int):
     return f'Update suppliers {suppliers_id}'


@suppliers.delete(f'/{suppliers_id}')
def delelte_suppliers(suppliers_id: int):
     return f'delete suppliers {suppliers_id}'