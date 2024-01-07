import os

# We can check the present working directory using the os.getcwd function.
print(os.getcwd())

# relative path
# lists all the files within current folder
# displays ['main.py', 'os_python_study_material.txt']
print(os.listdir('.'))

# absolute path
# lists all folder and files in specified folder
print(os.listdir('/New folder'))

# creates a new directory
# if the new folder to be created already exists , then the below command will throw error
# In order to solve above problem, exist_ok=True is used
# It runs the command even if the folder with that name already exists without modifying existing folder
os.makedirs("./makedir", exist_ok=True)
