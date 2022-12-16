from fastapi import APIRouter
from sql_base.models import Customer
import resolvers.customer

customer = APIRouter()


@customer.get('/')
def get_customer():
    return f'Response: {{text: Страница со списком заказов }}'


@customer.post('/')
def new_customer(customer: Customer,):
    new_id = resolvers.customer.new_customer(customer)
    return f'{{code: 201, id: {new_id}}}'


@customer.get(f'/{customer_id}')
def get_customer(customer_id: int):
    customer = resolvers.get_customer(customer_id)
    return 'customer: {customers_personal_information: пользовательская личностная информация, address: адрес}'


@customer.put(f'/{customer_id}')
def update_customer(customer_id: int):
     return f'Update customer {customer_id}'


@customer.delete(f'/{customer_id}')
def delelte_customer(customer_id: int):
     return f'delete customer {customer_id}'