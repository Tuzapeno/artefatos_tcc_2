import os
import random
import shutil

def create_subset(source_folder, dest_folder, fraction):
    """
    Creates a new folder with a random subset of images from a source folder.

    Args:
        source_folder (str): The path to the main dataset folder 
                             (containing 'Train' and 'Test' subfolders).
        dest_folder (str): The path to the new folder where the subset 
                           will be saved.
        fraction (float): The fraction of images to select (e.g., 0.1 for 10%).
    """
    # Create the destination folder if it doesn't exist
    if os.path.exists(dest_folder):
        print(f"Destination folder '{dest_folder}' already exists. Deleting it.")
        shutil.rmtree(dest_folder)
    os.makedirs(dest_folder)
    print(f"Created destination folder: {dest_folder}")

    # Process both 'Train' and 'Test' directories
    for split_name in ['Train', 'Test']:
        source_split_path = os.path.join(source_folder, split_name)
        dest_split_path = os.path.join(dest_folder, split_name)

        if not os.path.isdir(source_split_path):
            print(f"Warning: '{source_split_path}' not found. Skipping.")
            continue

        print(f"\nProcessing '{split_name}' directory...")

        # Get all class subdirectories (e.g., 'class_A', 'class_B')
        class_dirs = [d for d in os.listdir(source_split_path) if os.path.isdir(os.path.join(source_split_path, d))]

        for class_name in class_dirs:
            source_class_path = os.path.join(source_split_path, class_name)
            dest_class_path = os.path.join(dest_split_path, class_name)

            # Create the corresponding class directory in the destination
            os.makedirs(dest_class_path, exist_ok=True)

            # Get a list of all image files
            files = [f for f in os.listdir(source_class_path) if os.path.isfile(os.path.join(source_class_path, f))]
            
            # Shuffle the files randomly
            random.shuffle(files)

            # Calculate the number of files to select
            num_to_select = int(len(files) * fraction)
            
            # Select the subset of files
            selected_files = files[:num_to_select]

            # Copy the selected files to the new directory
            for file_name in selected_files:
                shutil.copy(os.path.join(source_class_path, file_name), dest_class_path)
            
            print(f"  - Copied {len(selected_files)} of {len(files)} images from class '{class_name}'.")

    print("\n✅ Subset creation complete!")

# --- HOW TO USE ---

# 1. Set the path to your original dataset
# source_dataset_path = './CNR-EXT-Patches-150x150/PATCHES/CNRPark-EXT/'
source_dataset_path = './PKLot/PKLotSegmented/'

# 2. Set the name for your new smaller dataset folder
# The script will create a folder like 'small_dataset_10_percent'
subset_name = 'small_dataset_pklot' 
# subset_name = 'small_dataset_cnrpark' 

# 3. Set the fraction of data you want (e.g., 0.1 for 10%, 0.25 for 25%)
subset_fraction = 0.05

# Construct the full destination path
destination_path = f"{subset_name}_{int(subset_fraction * 100)}_percent"

# Run the function
create_subset(source_dataset_path, destination_path, subset_fraction)
