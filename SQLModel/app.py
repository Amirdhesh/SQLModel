from engine import engine, create_table
from sqlmodel import Session, select
from Model import students, Departments


def Insert_operation():
    with Session(engine) as session:
        # Departments table
        dept1 = Departments(department="CSE")
        dept2 = Departments(department="ECE")
        # add more data
        session.add(dept1)
        session.add(dept2)
        session.commit()

        # Students table
        student1 = students(name="John", mail="John@mail.com", dept_id=dept2.id)
        student2 = students(name="Alice", mail="Alice@mail.com", dept_id=dept1.id)
        # add more data
        session.add(student1)
        session.add(student2)
        session.commit()


def Read_operation():
    with Session(engine) as session:
        statement = select(students)
        result = session.exec(statement)
        # for i in result:
        #     print(i)
        print(result)  # gives output in List format


def Read_where_operation():
    with Session(engine) as session:
        statement = select(students).where(students.name == "John")
        # result = session.get(students , 1 '''ID (primary key only)''') #selecting a single row by its Id column with the primary key
        result = session.exec(
            statement
        ).all()  # to read single row instead of all rows {.first() : "First row" , .one() : "to ensure there is only single row if there is more returns error"}
        for i in result:
            print(i)


def Read_limit_offset():
    with Session(engine) as session:
        statement = (
            select(students).where(students.name == "John").offset(1).limit(1)
        )  # offset is used skip 1 row and limit is used to limit upto 1 row (we need more data for this line of code to work)
        result = session.exec(statement).all()
        for i in result:
            print(i)


def Update_students():
    with Session(engine) as session:
        statement = select(students).where(students.name == "John")
        result = session.exec(statement)
        student = result.one()
        print(student)
        student.mail = "john1@mail.com"
        session.add(student)
        session.commit()
        print(student)


def Delete_student():
    with Session(engine) as session:
        statement = select(students).where(students.name == "John")
        result = session.exec(statement)
        student = result.one()
        session.delete(student)
        session.commit()
        print(student)  # prints the deleted object

        # To check :
        statement = select(students).where(students.name == "John")
        result = session.exec(statement)
        student = result.first()

        if student is None:
            print("There no row John")


def read_operation_connectedTable():
    with Session(engine) as session:
        statment = select(students, Departments).where(
            students.dept_id == Departments.id
        )
        result = session.exec(statment)
        for student, Department in result:
            print("Student :", student, "Department :", Department)


def update_operation_connectedTable():
    with Session(engine) as session:
        statment = select(students).where(students.name == "John")
        result = session.exec(statment)
        student = result.first()
        statment = select(Departments).where(Departments.department == "CSE")
        result = session.exec(statment)
        dept = result.one()
        student.dept_id = dept.id
        session.add(student)
        session.commit()


def delete_operation_connectedTable():
    with Session(engine) as session:
        statment = select(students).where(students.name == "John")
        result = session.exec(statment)
        student = result.first()
        student.dept_id = None
        session.add(student)
        session.commit()


read_operation_connectedTable()

if (
    __name__ == "__main__"
):  # This piece of code is executed when ever this app.py file is excuted
    create_table()
    # Insert_operation()
