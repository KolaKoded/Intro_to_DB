import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        # Connect to MySQL server
        cnx = mysql.connector.connect(
            user='your_username',
            password='your_password',
            host='your_host',
            port=your_port
        )
        cursor = cnx.cursor()

        # Attempt to create the database
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Access denied. Check your username and password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist.")
        else:
            print(f"An error occurred: {err}")
    else:
        cursor.close()
        cnx.close()

if __name__ == "__main__":
    create_database()
