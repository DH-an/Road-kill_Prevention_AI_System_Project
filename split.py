import os
import random
import shutil

# Define the path to the original data directory and the new split data directory
original_data_dir = 'test\images'
split_data_dir = 'test\split/data'

# Define the split ratio (e.g. 70% for training, 15% for validation, and 15% for testing)
train_ratio = 0.7
val_ratio = 0.15
test_ratio = 0.15

# Make the train, validation, and test directories
train_dir = os.path.join(split_data_dir, 'train')
val_dir = os.path.join(split_data_dir, 'val')
test_dir = os.path.join(split_data_dir, 'test')

os.makedirs(train_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# Loop through the original data directory and randomly assign each file to the train, validation, or test set
for root, dirs, files in os.walk(original_data_dir):
    for file in files:
        if file.endswith('.jpg') or file.endswith('.png'): # You can add more file formats if needed
            src_path = os.path.join(root, file)

            # Assign the file to the appropriate set
            r = random.random()
            if r < train_ratio:
                dst_dir = train_dir
            elif r < train_ratio + val_ratio:
                dst_dir = val_dir
            else:
                dst_dir = test_dir

            # Copy the file to the destination directory
            dst_path = os.path.join(dst_dir, os.path.splitext(file)[0] + os.path.splitext(src_path)[1])
            shutil.copy(src_path, dst_path)
