import mysql.connector


class BranchTable:
    def _init_(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def _del_(self):
        self.connection.close()

    def insert_branch(self, branch_data):
        query = "INSERT INTO branch (name, location) VALUES (%s, %s)"
        self.cursor.execute(query, branch_data)
        self.connection.commit()

    def update_branch(self, branch_id, new_data):
        query = "UPDATE branch SET name = %s, location = %s WHERE id = %s"
        self.cursor.execute(query, (*new_data, branch_id))
        self.connection.commit()
        