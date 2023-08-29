from typing import Self
import mysql.connector
import json

class BranchTable:
    def _init_(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

def update_branch(branch_id, new_name, new_city, new_franchise):
    query = "UPDATE branch SET branch_name = %s, branch_city = %s, branch_franchise = %s WHERE branch_id = %s"
    values = (new_name, new_city, new_franchise, branch_id)

# Güncelleme işlemi
branch_id_to_update = "4"
new_branch_name = "aaaa"
new_branch_city = "adana"
new_branch_franchise = "1"

update_branch(branch_id_to_update, new_branch_name, new_branch_city, new_branch_franchise)
Self.cursor.execute()
Self.connection.cursor()