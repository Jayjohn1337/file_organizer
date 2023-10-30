import os
import shutil

# Navigate to directory and list all the files
def list_files(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

directory = '(Insert PATH of Directoty)'
files = list_files(directory)

# Categorize files based on extensions
def categorize_files(files):
    file_dict = {}
    for file in files:
        file_extension = file.split('.')[-1]
        if file_extension not in file_dict:
            file_dict[file_extension] = []
        file_dict[file_extension].append(file)
    return file_dict

# Create folders for each category and move files
def organize_files(directory, file_dict):
    for ext, files in file_dict.items():
        folder_path = os.path.join(directory, ext)

        # Check if folder exists, if not, create it
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

        for file in files:
            file_path = os.path.join(directory, file)
            new_path = os.path.join(folder_path, file)

            # Skip if source and destination are the same
            if file_path == new_path:
                continue

            try:
                if os.path.exists(new_path):
                    print(f"File {new_path} already exists. Skipping.")
                else:
                    shutil.move(file_path, new_path)
            except PermissionError:
                print(f"Could not move {file} due to permission error.")
            except FileNotFoundError:
                print(f"Could not find {file}. Skipping.")


file_dict = categorize_files(files)
organize_files(directory, file_dict)

