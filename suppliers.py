from sql_base import base_worker
from sql_base import models


def new_suppliers(suppliers: models.suppliers) -> int:
    new_id = base_worker.insert_data("INSERT INTO suppliers(name_of_the_organization, address,)"
                                     "VALUES(?,?,?) "
                                     "RETURNING id",
                                     (suppliers.name_of_the_organization, suppliers.address,))
    return new_id