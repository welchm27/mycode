# the name of the import matches the file name (minus the .py)
# these two files MUST BE IN THE SAME DIRECTORY
import first_module

first_module.main() # add this to run the main function in first_module.py

print("Module #2 Name=", __name__)
