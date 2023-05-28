import os
import shutil

path = input("Enter Path:\n")
files = os.listdir(path)

for file in files:
    if os.path.isfile(os.path.join(path, file)):
        filename, extension = os.path.splitext(file)
        extension = extension[1:]

        destination_folder = os.path.join(path, extension)
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        
        shutil.move(os.path.join(path, file), os.path.join(destination_folder, file))