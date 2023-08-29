import mysql.connector
from database import get_db_config


def get_connection():
    db_config = get_db_config()
    return mysql.connector.connect(**db_config)


def create_branch(name, location, frenchise):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Branch (branch_name, branch_city,branch_frenchise) VALUES (%s, %s,%s)", (name, location, frenchise))
    conn.commit()
    conn.close()


def update_branch(branch_id, name, location, frenchise):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE Branch SET branch_name= %s, branch_city = %s, branch_frenshise=%s, WHERE id = %s",
                   (name, location, frenchise, branch_id))
    conn.commit()
    conn.close()


def delete_branch(branch_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Branch WHERE id = %s", (branch_id,))
    conn.commit()
    conn.close()


def fetch_branches():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Branch")
    branches = cursor.fetchall()
    conn.close()
    return branches