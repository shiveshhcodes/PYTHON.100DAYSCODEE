import os
import shutil
import time


def ensure_py_extension(filename):
    if not filename.endswith('.py'):
        filename += '.py'
    return filename

while True:

    source_file = input("ENTER SOURCE FILE - ")
    if source_file.lower()=="quit":
        break
    else:
     pass
    copy_destination_file = input("ENTER DESTINATION FILE - ")

    source_file = ensure_py_extension(source_file)
    copy_destination_file = ensure_py_extension(copy_destination_file)

    source = f"/Users/shiveshrichhariya/Desktop/GITHUB/100 DAYS OF CODE/PYTHON.100DAYSCODE/Tkinter Learning/{source_file}"
    destination = f"/Users/shiveshrichhariya/Desktop/GITHUB/100 DAYS OF CODE/PYTHON.100DAYSCODE/Tkinter Learning/{copy_destination_file}"

    # print(f"Source path: {source}")
    # print(f"Destination path: {destination}")

    destination_dir = os.path.dirname(destination)
    if not os.path.exists(destination_dir):
        print(f"Creating directory: {destination_dir}")
        os.makedirs(destination_dir)

    if os.path.exists(source):
        # print(f"Copying file from {source} to {destination}")
        # time.sleep(1.3)
        print("Processingggggg!! ⏳")
        shutil.copy(source, destination)
        # time.sleep(1.34)
        print("Done Shivesh Boss")
        
    else:
     print(f"Source file does not exist , please try again")
    time.sleep(1)
    
