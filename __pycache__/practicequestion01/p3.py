import os
directory_path='/python'
contents = os.listedir(directory_path)
for item in contents:
    print(item)