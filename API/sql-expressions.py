from sqlalchemy import (
    create_engine, Table, Column, Float, Date, Time, ForeignKey, Integer, String, Boolean, MetaData
)

# executing the instructions from our localhost "eatatjoes" db
db = create_engine("postgresql:///eatatjoes")

meta = MetaData(db)

# create variable for "Tables" table
table_table = Table(
    "Tables", meta,
    Column("TableId", Integer, primary_key=True),
    Column("TableNumber", Integer),
    Column("Capacity", Integer),
    Column("Location", String),
    Column("AvaliabiltyStatus", Boolean),
)

# create variable for "Customers" table
customers_table = Table(
    "Customers", meta,
    Column("CustomerId", Integer, primary_key=True),
    Column("FirstName", String),
    Column("LastName", String),
    Column("PhoneNumber", String),
    Column("EmailAddress", String),
)

# create variable for "Reservations" table
reservations_table = Table(
    "Reservations", meta,
    Column("ReservationId", Integer, primary_key=True),
    Column("CustomerId", Integer, ForeignKey("customers_table.CustomerId")),
    Column("TableId", Integer, ForeignKey("table_table.TableId")),
    Column("ReservationDate", Date),
    Column("ReservationTime", Time),
    Column("NumberOfGuests", Integer),
)

# making the connection
with db.connect() as connection:

    # Query 1 - select all data from the "table" table
    select_query = table_table.select()

    # Query 2 - select only the "Name" column from the "Artist" table
    # select_query = artist_table.select().with_only_columns([artist_table.c.Name])

    # Query 3 - select only 'Queen' from the "Artist" table
    # select_query = artist_table.select().where(artist_table.c.Name == "Queen")

    # Query 4 - select only by 'ArtistId' #51 from the "Artist" table
    # select_query = artist_table.select().where(artist_table.c.ArtistId == 51)

    # Query 5 - select only the albums with 'ArtistId' #51 on the "Album" table
    # select_query = album_table.select().where(album_table.c.ArtistId == 51)

    # Query 6 - select all tracks where the composer is 'Queen' from the "Track" table
    # select_query = track_table.select().where(track_table.c.Composer == "Queen")

    results = connection.execute(select_query)
    for result in results:
        print(result)