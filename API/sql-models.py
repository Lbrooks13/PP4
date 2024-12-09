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


# Query 1 - select all records from the "Artist" table
tables = session.query(Table)
for table in tables:
    print(table.TableId, table.Capacity, sep=" | ")

# Query 2 - select only the "Name" column from the "Artist" table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.Name)

# Query 3 - select only "Queen" from the "Artist" table
# artist = session.query(Artist).filter_by(Name="Queen").first()
# print(artist.ArtistId, artist.Name, sep=" | ")

# Query 4 - select only by "ArtistId" #51 from the "Artist" table
# artist = session.query(Artist).filter_by(ArtistId=51).first()
# print(artist.ArtistId, artist.Name, sep=" | ")

# Query 5 - select only the albums with "ArtistId" #51 on the "Album" table
# albums = session.query(Album).filter_by(ArtistId=51)
# for album in albums:
#     print(album.AlbumId, album.Title, album.ArtistId, sep=" | ")

# Query 6 - select all tracks where the composer is "Queen" from the "Track" table
# tracks = session.query(Track).filter_by(Composer="Queen")
# for track in tracks:
#     print(
#         track.TrackId,
#         track.Name,
#         track.AlbumId,
#         track.MediaTypeId,
#         track.GenreId,
#         track.Composer,
#         track.Milliseconds,
#         track.Bytes,
#         track.UnitPrice,
#         sep=" | "
#     )