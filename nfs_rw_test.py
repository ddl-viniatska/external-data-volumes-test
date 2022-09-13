import os
import uuid

unique_filename = str(uuid.uuid4())

# Specify the directory path
path = r'/domino/edv/diabetes'

file_name = unique_filename

# Print file to be created
print(unique_filename)

# Creating a file at specified folder
with open(os.path.join(path, file_name), 'w') as fp:
    fp.write('Test passed')

print(os.listdir(path))

# verify file exist
filepath = os.path.join(path,unique_filename)
print(os.path.isfile(filepath))


# print the contents of a file
with open(filepath, 'r') as f:
    print(f.read())
