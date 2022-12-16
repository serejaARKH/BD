from fastapi import APIRouter
from sql_base.models import Orders
import resolvers.orders

orders = APIRouter()


@orders.get('/')
def get_orders():
    return f'Response: {{text: Страница со списком сотрудников }}'


@orders.post('/')
def new_orders(orders: Orders,):
    new_id = resolvers.orders.new_orders(orders)
    return f'{{code: 201, id: {new_id}}}'


@orders.get(f'/{orders_id}')
def get_orders(orders_id: int):
    orders = resolvers.get_orders(orders_id)
    return 'orders: {customers_personal_information: пользовательская личностная информация, address: адрес}'


@orders.put(f'/{orders_id}')
def update_orders(orders_id: int):
     return f'Update orders {orders_id}'


@orders.delete(f'/{orders_id}')
def delelte_orders(orders_id: int):
     return f'delete orders {orders_id}'