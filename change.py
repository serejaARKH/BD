from sql_base import base_worker
from sql_base import models


def new_change(change: models.change) -> int:
    new_id = base_worker.insert_data("INSERT INTO change(сontract_id, order_id, supplier_id, responsible_demployee_id, name_of_works, work_id, price_per_unit_of_measurement, square_footage, material_id, customer_id, warehouse_id)"
                                     "VALUES(?,?,?) "
                                     "RETURNING id",
                                     (change.сontract_id, change.order_id, change.supplier_id, change.responsible_demployee_id, change.name_of_works, change.work_id, change.price_per_unit_of_measurement, change.square_footage, change.material_id, change.customer_id, change.warehouse_id))
    return new_id