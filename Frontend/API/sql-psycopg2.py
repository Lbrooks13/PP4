import psycopg2


# connect to "eatatjoes" database
connection = psycopg2.connect(database="eatatjoes")

# build a cursor object of the database
cursor = connection.cursor()

# Query 1 - select all tables from the "Tables" table
cursor.execute('SELECT "AvaliabiltyStatus" FROM "Tables"')

# fetch the results (multiple)
results = cursor.fetchall()

# fetch the result (single)
# results = cursor.fetchone()

# close the connection
connection.close()

# print results
for result in results:
    print(result)