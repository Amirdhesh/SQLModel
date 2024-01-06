from engine import engine , create_table
from sqlmodel import Session , select
from Model import students
def Insert_operation():
    student1 = students(name="John" , mail="John@mail.com")
    student2 = students(name="Alice" ,mail= "Alice@mail.com")
    # add more data 
    with Session(engine) as session : 
        session.add(student1)
        session.add(student2)
        session.commit()


def Read_operation():
    with Session(engine) as session:
        statement = select(students)
        result = session.exec(statement)
        # for i in result: 
        #     print(i)
        print(result) #gives output in List format 


def Read_where_operation():
    with Session(engine) as session:
        statement = select(students).where(students.name == "John")
        #result = session.get(students , 1 '''ID (primary key only)''') #selecting a single row by its Id column with the primary key
        result = session.exec(statement).all() #to read single row instead of all rows {.first() : "First row" , .one() : "to ensure there is only single row if there is more returns error"}
        for i in result:
             print(i)


def Read_limit_offset():
    with Session(engine) as session:
        statement = select(students).where(students.name == "John").offset(1).limit(1) #offset is used skip 1 row and limit is used to limit upto 1 row (we need more data for this line of code to work)
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
        student= result.one()
        session.delete(student)
        session.commit()
        print(student) #prints the deleted object


        #To check :
        statement = select(students).where(students.name == "John")
        result = session.exec(statement)
        student= result.first

        if student is None:
            print("There no row John")

Delete_student()

if __name__ == "__main__":
    create_table() #func is called once when ever this engine.py file is excuted
    #Insert_operation()