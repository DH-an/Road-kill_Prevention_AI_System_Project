import os
import shutil

dir1 = 'test\\split\\data\\val'  # first folder
dir2 = 'test\\labels'  # second folder
output_dir = 'output'  # output folder to save matching files

# create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# get a list of files in the first directory
files1 = [f for f in os.listdir(dir1) if os.path.isfile(os.path.join(dir1, f))]

# get a list of files in the second directory
files2 = [f for f in os.listdir(dir2) if os.path.isfile(os.path.join(dir2, f))]

# loop through each file in the first directory
for file1 in files1:
    # get the filename without the extension
    name1, ext1 = os.path.splitext(file1)

    # loop through each file in the second directory
    for file2 in files2:
        # get the filename without the extension
        name2, ext2 = os.path.splitext(file2)

        # if the filenames match (excluding the extension)
        if name1 == name2:
            # copy the matching files to the output directory
            #shutil.copy2(os.path.join(dir1, file1), os.path.join(output_dir, file1))
            shutil.copy2(os.path.join(dir2, file2), os.path.join(output_dir, file2))
