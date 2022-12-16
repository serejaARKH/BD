from typing import Optional
from pydantic import BaseModel

class change(BaseModel):
    shift_id: Optional[int]
    сontract_id: int
    order_id: int
    supplier_id: int
    responsible_demployee_id: int
    name_of_works: str
    work_id: int
    price_per_unit_of_measurement: int
    square_footage: int
    material_id: int
    customer_id: int
    warehouse_id: int

class orders(BaseModel):
    order_id: Optional[int]
    customers_personal_information: str
    address: str
    shift_id: int

class materials(BaseModel):
    material_id: Optional[int]
    names: str
    price: int
    material_type_id: int

class suppliers(BaseModel):
    suppliers_id: Optional[int]
    name_of_the_organization:str
    address: str

class contract(BaseModel):
    contract_id: Optional[int]
    personal_information: str
    date_of_conclusion: str
    shift_id: str
    customer_id: str

class price_list(BaseModel):
    work_id: Optional[int]
    name_of_works: int
    price_per_unit_measurement: str

class customer(BaseModel):
    customer_id: Optional[int]
    names: str
    full_name: str
    personal_information: str
    address: str
    type: str
    kPP: str
    iNN: str
    telephone: int
    passport: str

class staff(BaseModel):
    employee_id: Optional[int]
    name: str
    full_name: str
    date_of_birth: int
    experience: str
    post: str

class warehouse(BaseModel):
    warehouse_id: Optional[int]
    n_warehouse: int
    address: str
    name_of_the_material: str
    remains: int
    supplier: str



