import psycopg2
from config import config

"""
connection = psycopg2.connect(
    host="localhost", port="5432", database="restaurant_management",
    user="postgres", password="test123")

This is one way of doing it but its not used in real situations
The database.ini approach is better and right way of doing it
"""


def connect():
    connection = None

    try:
        params = config()
        print('\nConnection to the postgreSQL database ...')
        connection = psycopg2.connect(**params)

        #create a cursor
        crsr = connection.cursor()
        print('PostgreSQL database version: ')
        crsr.execute('SELECT version()')
        db_version = crsr.fetchone()
        print(db_version)

        """
            The cursor and the connection are the communication between python file and the database.
            In the end i need to close them both
        """

        crsr.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if connection is not None:
            connection.close()
            print('Database connection terminated.\n')


if __name__ == "__main__":
    connect()