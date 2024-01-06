import Model
from sqlmodel import SQLModel , create_engine
import os
from load_dotenv import load_dotenv

load_dotenv()

engine = create_engine(os.getenv('mysqllink'))


def create_table():
    SQLModel.metadata.create_all(engine)
