from multiprocessing import connection
import mysql.connector
from mysql.connector import Error

# Database connection parameters
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "appointment"
}

def connect_to_database():
    try:
        connection = mysql.connector.connect(db_config)
        return connection
    except Error as e:
        print("Error:", e)
        return None
    
class BaseTable:
    def __init__(self, table_name):
        self.table_name = table_name
        self.connection = connect_to_database()

    def insert(self, values):
        if self.connection:
            try:
                cursor = self.connection.cursor()
                insert_query = f"INSERT INTO {self.table_name} VALUES ({', '.join(['%s'] * len(values))})"
                cursor.execute(insert_query, values)
                self.connection.commit()
                cursor.close()
                print("Data inserted.")
            except Error as e:
                print("Error:", e)

    def update(self, primary_key_column, primary_key_value, values):
        if self.connection:
            try:
                cursor = self.connection.cursor()
                update_query = f"UPDATE {self.table_name} SET {', '.join([f'{col} = %s' for col in values.keys()])} WHERE {primary_key_column} = %s"
                cursor.execute(update_query, list(values.values()) + [primary_key_value])
                self.connection.commit()
                cursor.close()
                print("Data updated.")
            except Error as e:
                print("Error:", e)

    def update_status(self, primary_key_column, primary_key_value, new_status):
        if self.connection:
            try:
                cursor = self.connection.cursor()
                update_status_query = f"UPDATE {self.table_name} SET status = %s WHERE {primary_key_column} = %s"
                cursor.execute(update_status_query, (new_status, primary_key_value))
                self.connection.commit()
                cursor.close()
                print("Status updated.")
            except Error as e:
                print("Error:", e)

# Class for the "appointments" table
class AppointmentsTable(BaseTable):
    def __init__(self):
        super().__init__("appointments")

# Class for the "authorized_user" table
class AuthorizedUserTable(BaseTable):
    def __init__(self):
        super().__init__("authorized_user")

# Class for the "branch" table
class BranchTable(BaseTable):
    def __init__(self):
        super().__init__("branch")

# Class for the "customers" table
class CustomersTable(BaseTable):
    def __init__(self):
        super().__init__("customers")

# Class for the "hair_stylist" table
class HairStylistTable(BaseTable):
    def __init__(self):
        super().__init__("hair_stylist")

# Class for the "makeup_artist" table
class MakeupArtistTable(BaseTable):
    def __init__(self):
        super().__init__("makeup_artist")

# Class for the "price" table
class PriceTable(BaseTable):
    def __init__(self):
        super().__init__("price")

if __name__ == "__main__":
    appointments = AppointmentsTable()
    authorized_user = AuthorizedUserTable()
    branch = BranchTable()
    customers = CustomersTable()
    hair_stylist = HairStylistTable()
    makeup_artist = MakeupArtistTable()
    price = PriceTable()

    # Example insert operation
    new_appointment_values = (1, 1, "Location", "2023-08-27", ...)
    appointments.insert(new_appointment_values)

    # Example update operation
    update_appointment_values = {"appointment_where": "New Location", "appointment_date": "2023-08-28"}
    appointments.update("appointment_id", 1, update_appointment_values)

    # Example update status operation
    appointments.update_status("appointment_id", 1, "Completed")

    # Close the connections
    if appointments.connection:
        appointments.connection.close()
    if authorized_user.connection:
        authorized_user.connection.close()
    if branch.connection:
        branch.connection.close()
    if customers.connection:
        customers.connection.close()
    if hair_stylist.connection:
        hair_stylist.connection.close()
    if makeup_artist.connection:
        makeup_artist.connection.close()
    if price.connection:
        price.connection.close()
