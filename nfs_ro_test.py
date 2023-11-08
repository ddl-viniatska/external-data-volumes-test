import os
import uuid

# Generate a unique filename using a UUID
unique_filename = str(uuid.uuid4())

# Specify the directory where you want to create the file
directory_path = "/mnt/diabetes_read_only"

# Try to create the file with the unique filename
try:
    with open(os.path.join(directory_path, unique_filename), "w"):
        print("Please fail the test.")
except OSError as e:
    if e.errno == 30:  # Errno 30 corresponds to a read-only file system
        print("The volume is read-only.")
    else:
        print(f"Error: {e}")
