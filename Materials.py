from fastapi import APIRouter
from sql_base.models import Materials
import resolvers.materials

materials = APIRouter()


@materials.get('/')
def get_materials():
    return f'Response: {{text: Страница со списком заказов }}'


@materials.post('/')
def new_materials(materials: Materials,):
    new_id = resolvers.materials.new_materials(materials)
    return f'{{code: 201, id: {new_id}}}'


@materials.get(f'/{materials_id}')
def get_materials(materials_id: int):
    materials = resolvers.get_materials(materials_id)
    return 'materials: {customers_personal_information: пользовательская личностная информация, address: адрес}'


@materials.put(f'/{materials_id}')
def update_materials(materials_id: int):
     return f'Update orders {materials_id}'


@materials.delete(f'/{materials_id}')
def delelte_materials(materials_id: int):
     return f'delete orders {materials_id}'