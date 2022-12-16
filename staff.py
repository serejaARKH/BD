from sql_base import base_worker
from sql_base import models


def new_staff(staff: models.staff) -> int:
    new_id = base_worker.insert_data("INSERT INTO warehouse(name, full_name, date_of_birth, experience, post)"
                                     "VALUES(?,?,?) "
                                     "RETURNING id",
                                     (staff.name, staff.full_name, staff.date_of_birth, staff.experience, staff.post))
    return new_id