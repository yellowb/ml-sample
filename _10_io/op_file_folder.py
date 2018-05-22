# Sample to operate file and folder


import os

# current folder
current_dir_path = os.path.abspath('.')
print(current_dir_path)

# project folder
project_dir_path = os.path.abspath('..')
print(project_dir_path)

# list all folders in project folder
all_folders = [x for x in os.listdir('..') if os.path.isdir(os.path.join(project_dir_path, x))]
print(all_folders)

# list all .py files in current folder
all_py_files = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
print(all_py_files)

