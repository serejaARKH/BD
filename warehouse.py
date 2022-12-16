from sql_base import base_worker
from sql_base import models


def new_warehouse(warehouse: models.warehouse) -> int:
    new_id = base_worker.insert_data("INSERT INTO warehouse(address, name_of_the_material, remains, supplier)"
                                     "VALUES(?,?,?) "
                                     "RETURNING id",
                                     (warehouse.address, warehouse.name_of_the_material, warehouse.remains, warehouse.supplier))
    return new_id