from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String, Boolean, Date, Time
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "eatatjoes" database
db = create_engine("postgresql:///eatatjoes")
base = declarative_base()


# create a class-based model for the "Table" table
class Table(base):
    __tablename__ = "Tables"
    TableId = Column(Integer, primary_key=True)
    TableNumber = Column(Integer)
    Capacity = Column(Integer)
    Location = Column(String)
    AvaliabiltyStatus = Column(Boolean)


# create a class-based model for the "Customers" table
class Customer(base):
    __tablename__ = "Customers"
    CustomerId = Column(Integer, primary_key=True)
    FirstName = Column(String)
    LastName = Column(String)
    PhoneNumber = Column(String)
    EmailAddress = Column(String)


# create a class-based model for the "Reservations" table
class Reservation(base):
    __tablename__ = "Reservations"
    ReservationId = Column(Integer, primary_key=True)
    CustomerId = Column(Integer, ForeignKey("Customer.CustomerId"))
    TableId = Column(Integer, ForeignKey("Table.TableId"))
    ReservationDate = Column(Date)
    ReservationTime = Column(Time)
    NumberOfGuests = Column(Integer)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)


# Query 1 - select all records from the "Table" table
tables = session.query(Table)
for table in tables:
    print(table.TableId, table.Capacity, sep=" | ")
