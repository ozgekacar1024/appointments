from database import get_db_config
import mysql.connector


class BranchDatabase:
    def _init_(self):
        self.db_config = get_db_config()

    def get_connection(self):
        return mysql.connector.connect(**self.db_config)

    def create_branch(self, name, location, frenchise):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Branch (branch_name, branch_city,branch_frenchise) VALUES (%s, %s,%s)", (name, location, frenchise))
        conn.commit()
        conn.close()

    def update_branch(self, branch_id, name, location, frenchise):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE Branch SET branch_name =%s, branch_city= %s, branch_frenchise= %s, WHERE id = %s", (name, location, frenchise, branch_id))
        conn.commit()
        conn.close()

    def delete_branch(self, branch_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE Branch SET status = %s WHERE id = %s", ("0", branch_id))
        conn.commit()
        conn.close()

    def fetch_branches(self):
        conn = self.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Branch WHERE status = %s", ("1",))
        branches = cursor.fetchall()
        conn.close()
        return branches