from sql_base import base_worker
from sql_base import models


def new_contract(contract: models.contract) -> int:
    new_id = base_worker.insert_data("INSERT INTO contract(personal_information, date_of_conclusion, shift_id, customer_id)"
                                     "VALUES(?,?,?) "
                                     "RETURNING id",
                                     (contract.personal_information, contract.date_of_conclusion, contract.date_of_birth, contract.shift_id, contract.customer_id))
    return new_id