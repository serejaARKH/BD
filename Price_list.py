from fastapi import APIRouter
from sql_base.models import Price_list
import resolvers.Price_list

price_list = APIRouter()


@price_list.get('/')
def get_price_list():
    return f'Response: {{text: Страница со списком заказов }}'


@price_list.post('/')
def new_price_list(price_list: Price_list,):
    new_id = resolvers.price_list.new_price_list(price_list)
    return f'{{code: 201, id: {new_id}}}'


@price_list.get(f'/{price_list_id}')
def get_price_list(price_list_id: int):
    price_list = resolvers.get_price_list(price_list_id)
    return 'price_list: {name_of_works: название работы, price_per_unit_measurement:цена за еденицу измерения}'


@price_list.put(f'/{price_list_id}')
def update_price_list(price_list_id: int):
     return f'Update price_list {price_list_id}'


@price_list.delete(f'/{price_list_id}')
def delelte_price_list(price_list_id: int):
     return f'delete price_list {price_list_id}'