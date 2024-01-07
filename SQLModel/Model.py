from typing import Optional
from sqlmodel import Field, SQLModel


class Departments(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    department: str


class students(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)  # added Index
    mail: str = Field(unique=True)
    dept_id: Optional[int] = Field(default=None, foreign_key="departments.id")
