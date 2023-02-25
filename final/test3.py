import os

os.chdir('/home/pi/camera')

file_names = os.listdir()

for filename in file_names:
        for i in range(2):
                print(os.path.splitext(filename)[0])
        break;
