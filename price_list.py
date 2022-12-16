from sql_base import base_worker
from sql_base import models


def new_price_list(price_list: models.price_list) -> int:
    new_id = base_worker.insert_data("INSERT INTO price_list(name_of_works, price_per_unit_measurement)"
                                     "VALUES(?,?,?) "
                                     "RETURNING id",
                                     (price_list.name_of_works, price_list.price_per_unit_measurement))
    return new_id