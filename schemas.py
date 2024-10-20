from pydantic import BaseModel
from datetime import datetime


class User(BaseModel):

    gender: str
    first_name: str
    last_name: str
    father_name: str
    date_of_birth: datetime
    national_code: str
    phone_number: str
    role_id: int | None = None
    recruitment_date: datetime
    is_super_admin: bool
    is_panel_user: bool
    permission_group_id: int | None = None
    is_enabled: bool
    recorder_id: int | None = None


class UserCreate(User):
    pass


class UserUpdate(User):
    pass
