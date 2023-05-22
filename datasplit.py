import os
import random

data_dir = "test" #Set your data directory path
train_ratio = 0.8  # Set your train data ratio[]

# Create train and val directories if they don't exist
os.makedirs(os.path.join(data_dir, "train"), exist_ok=True)
os.makedirs(os.path.join(data_dir, "val"), exist_ok=True)


# Get list of image filenames
image_files = [f for f in os.listdir(os.path.join(data_dir, "images")) if f.endswith(".jpg")]

# Shuffle image filenames
random.shuffle(image_files)

# Split image filenames into train and val sets
train_size = int(len(image_files) * train_ratio)
train_files = image_files[:train_size]
val_files = image_files[train_size:]


# Copy train and val images to respective directories
for file in train_files:
    os.replace(os.path.join(data_dir, "images", file), os.path.join(data_dir, "train", file))
for file in val_files:
    os.replace(os.path.join(data_dir, "images", file), os.path.join(data_dir, "val", file))

# Copy corresponding train and val labels to respective directories
for file in train_files:
    os.replace(os.path.join(data_dir, "labels", file.replace(".jpg", ".txt")), os.path.join(data_dir, "train", file.replace(".jpg", ".txt")))
for file in val_files:
    os.replace(os.path.join(data_dir, "labels", file.replace(".jpg", ".txt")), os.path.join(data_dir, "val", file.replace(".jpg", ".txt")))
