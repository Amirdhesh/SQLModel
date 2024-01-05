import Model
from sqlmodel import SQLModel , create_engine
import os
from load_dotenv import load_dotenv

load_dotenv()

engine = create_engine(os.getenv('mysqllink'))


def create_database_and_table():
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    create_database_and_table() #func is called once when ever this engine.py file is excuted
