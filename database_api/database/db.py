import psycopg2
import os

def get_connection():
    return psycopg2.connect(
        host='localhost',
        database='postgres',
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD']
    )
