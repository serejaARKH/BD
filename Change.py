from fastapi import APIRouter
from sql_base.models import Change
import resolvers.change

change = APIRouter()


@change.get('/')
def get_change():
    return f'Response: {{text: Страница со списком заказов }}'


@change.post('/')
def new_change(change: Change,):
    new_id = resolvers.change.new_change(change)
    return f'{{code: 201, id: {new_id}}}'


@change.get(f'/{change_id}')
def get_change(change_id: int):
    change = resolvers.get_change(change_id)
    return 'change: {customers_personal_information: пользовательская личностная информация, address: адрес}'


@change.get(f'/{change_id}')
def update_change(change_id: int):
     return f'Update change {change_id}'


@change.delete(f'/{change_id}')
def delelte_change(change_id: int):
     return f'delete change {changea_id}'