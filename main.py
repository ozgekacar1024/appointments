from database import AppointmentDatabase
from branch import BranchTable
import json

# JSON dosyasını okuma
with open('config.json') as json_file:
    db_config = json.load(json_file)

# Create the appointment database if it doesn't exist
appointment_db = AppointmentDatabase(**db_config)
appointment_db.create_database()

branch_table = BranchTable(**db_config)

# Insert a new branch
branch_data = ("Branch A", "City X")
branch_table.insert_branch(branch_data)

# Update a branch
branch_table.update_branch(1, ("New Branch Name", "New Location"))