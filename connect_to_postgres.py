import psycopg2

try:
    conn = psycopg2.connect(host="localhost", database="pythontest_db",
                            user="docker", password="docker")
except Exception as e:
    print(e)
    exit(0)


if conn is not None:
    print('Connection established to PostgreSQL.')

    # Creating a cursor
    cur = conn.cursor()

    # Getting a query ready.
    cur.execute('SELECT * from DOCUMENT_TEMPLATE limit 3;')

    # we are fetching all the data from the query above.
    get_all_data = cur.fetchall()

    # Print all data
    print(get_all_data)

    # Close connection
    conn.close()
else:
    print('Connection not established to PostgreSQL.')