from fastapi import APIRouter
from sql_base.models import Contract
import resolvers.contract

contract = APIRouter()


@contract.get('/')
def get_contract():
    return f'Response: {{text: Страница со списком заказов }}'


@contract.post('/')
def new_contract(contract: Contract,):
    new_id = resolvers.contract.new_contract(contract)
    return f'{{code: 201, id: {new_id}}}'


@contract.get(f'/{contract_id}')
def get_contract(contract_id: int):
    contract = resolvers.get_contract(contract_id)
    return 'contract: {customers_personal_information: пользовательская личностная информация, address: адрес}'


@contract.put(f'/{contract_id}')
def update_contract(contract_id: int):
     return f'Update contract {contract_id}'


@contract.delete(f'/{contract_id}')
def delelte_contract(contract_id: int):
     return f'delete contract {contract_id}'