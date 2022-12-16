from sql_base import base_worker
from sql_base import models


def new_customer(customer: models.customer) -> int:
    new_id = base_worker.insert_data("INSERT INTO customer(names, full_name, personal_information, address, type, kPP, iNN, telephone, passport)"
                                     "VALUES(?,?,?) "
                                     "RETURNING id",
                                     (customer.names, customer.full_name, customer. personal_information, customer.address, customer.type, customer.kPP, customer.iNN, customer.telephone, customer.passport))
    return new_id