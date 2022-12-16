from sql_base import base_worker
from sql_base import models


def new_orders(orders: models.orders) -> int:
    new_id = base_worker.insert_data("INSERT INTO orders(orders_id, address, shift_id)"
                                     "VALUES(?,?,?) "
                                     "RETURNING id",
                                     (orders.orders_id, orders.address, orders.shift_id))
    return new_id