import os

path = 'w'  # replace with the path to your directory

for filename in os.listdir(path):
    if filename.endswith('.jpg'):
        os.rename(os.path.join(path, filename), os.path.join(path, os.path.splitext(filename)[0] + '_D.jpg'))
