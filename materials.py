from sql_base import base_worker
from sql_base import models


def new_materials(materials: models.materials) -> int:
    new_id = base_worker.insert_data("INSERT INTO materials(names,  price, material_type_id,)"
                                     "VALUES(?,?,?) "
                                     "RETURNING id",
                                     (materials.names, materials.price, materials.material_type_id))
    return new_id