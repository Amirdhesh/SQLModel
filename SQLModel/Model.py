from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship


class Departments(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    department: str
    students: List["students"] = Relationship(back_populates="department_name")


class students(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)  # added Index
    mail: str = Field(unique=True)
    dept_id: Optional[int] = Field(default=None, foreign_key="departments.id")
    department_name: List["Departments"] = Relationship(back_populates="students")
