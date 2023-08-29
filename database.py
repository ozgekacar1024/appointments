import mysql.connector
import json


class AppointmentDatabase:
    def _init_(self):
        with open('config.json') as json_file:
            db_config = json.load(json_file)
        self.connection = mysql.connector.connect(
            host=db_config['database']['host'],
            user=db_config['database']['user'],
            password=db_config['database']['password'],
            database=db_config['database']['database'],
        )
        
        self.cursor = self.connection.cursor()

    def _del_(self):
        self.connection.close()

    def create_database(self):
        query = "CREATE DATABASE IF NOT EXISTS appointment_db"
        self.cursor.execute(query)
        self.connection.commit()