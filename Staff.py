from fastapi import APIRouter
from sql_base.models import Staff
import resolvers.staff

staff = APIRouter()


@staff.get('/')
def get_staff():
    return f'Response: {{text: Страница со списком персонала }}'


@staff.post('/')
def new_staff(staff: Staff,):
    new_id = resolvers.staff.new_staff(staff)
    return f'{{code: 201, id: {new_id}}}'


@staff.get('/{staff_id}')
def get_staff(staff_id: int):
    staff = resolvers.get_staff(staff_id)
    return 'staff: {names: имя , full_name: Ф.И.О , date_of_brith: год рождения , experience: опыт работы , post: должность}'


@staff.put('/{staff_id}')
def update_staff(staff_id: int):
     return f'Update staff {staff_id}'


@staff.delete(f'/{staff_id}')
def delelte_staff(staff_id: int):
     return f'delete staff {staff_id}'