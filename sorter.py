import os
import shutil

EMPTY = 0
OCCUPIED = 1

directory_name = "CNRPark-EXT"
label_file = "all.txt"
label_path = f"./LABELS/{label_file}"
file_path = "./PATCHES"

train_dir = "Train"
test_dir = "Test"

num_lines = 0

def copy_file(path, label, Type):
    target_path = ""
    file_name = os.path.basename(path)

    if int(label) == EMPTY:
        target_path = f"{directory_name}/{Type}/Empty/{file_name}"
    elif int(label) == OCCUPIED:
        target_path = f"{directory_name}/{Type}/Occupied/{file_name}"

    source_path = f"{file_path}/{path}"

    # print(f"Copying {source_path} to {target_path}")
    shutil.move(source_path, target_path)


def check_and_create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

# MAIN ==============================

check_and_create_dir(directory_name)
check_and_create_dir(f"./{directory_name}/{train_dir}/Empty")
check_and_create_dir(f"./{directory_name}/{train_dir}/Occupied")
check_and_create_dir(f"./{directory_name}/{test_dir}/Empty")
check_and_create_dir(f"./{directory_name}/{test_dir}/Occupied")

# Retrieve the number of lines in the file
with open(label_path, 'r') as file:
    num_lines = sum(1 for _ in file)
print(f"Number of lines in {label_path}: {num_lines}")

half = num_lines // 2
i = 0

num_training = 0
num_testing = 0

# Process the file and print paths based on labels
with open(label_path, 'r') as file:
    for line in file:
        path, label = line.split()
        if i < half:
            copy_file(path, label, "Train")
            num_training += 1
        else:
            copy_file(path, label, "Test")
            num_testing += 1
        i += 1
        
        if i % 10000 == 0:
            print(f"Processed {i} / {num_lines} files...")
        
print(f"Number of training samples: {num_training}\n")
print(f"Number of testing samples: {num_testing}\n")
print(f"Total samples processed: {num_training + num_testing}\n")