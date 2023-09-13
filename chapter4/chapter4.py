import swimclub
import os
swim_files = os.listdir(swimclub.FOLDER)
swim_files.remove(".DS_Store")

for f in swim_files:
    print("Processing", f)
    data = swimclub.read_swim_data(f)
    #print(data)