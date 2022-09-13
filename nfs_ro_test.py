import os
import uuid

unique_filename = str(uuid.uuid4())

# Specify the directory path
path = r'/mnt/diabetes_read_only'
filename = "demo.csv"

print(os.listdir(path))

# verify file exist
filepath = os.path.join(path,filename)
print(os.path.isfile(filepath))
