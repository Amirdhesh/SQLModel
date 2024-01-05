from typing import Optional
from sqlmodel import Field, SQLModel


class students(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    mail: str = Field(unique=True)
