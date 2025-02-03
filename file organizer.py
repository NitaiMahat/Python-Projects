import os
import shutil
import hashlib
import re

# Define the main directory to organize
main_directory = os.path.join(os.path.expanduser("~"), "Downloads")

# Define file extensions and their corresponding folder names
extensions = {
    ".pdf": "DOCUMENTS",
    ".txt": "DOCUMENTS",
    ".docx": "DOCUMENTS",
    ".doc": "DOCUMENTS",
    ".php": "DOCUMENTS",
    ".rtf": "DOCUMENTS",
    ".epub": "DOCUMENTS",
    ".azw3": "DOCUMENTS",
    ".webp": "DOCUMENTS",
    ".pptx": "DOCUMENTS",
    ".xlsx": "DOCUMENTS",
    ".jpg": "IMAGES",
    ".jpeg": "IMAGES",
    ".gif": "IMAGES",
    ".jfif": "IMAGES",
    ".png": "IMAGES",
    ".mp4": "VIDEOS",
    ".m4a": "VIDEOS",
    ".mov": "VIDEOS",
    ".py": "PYTHON",
    ".exe": "APPLICATIONS",
    ".zip": "ZIPFILE",
    ".mp3": "MUSIC"
}

# Function to calculate the hash of a file (for duplicate detection by content)
def calculate_hash(file_path):
    hasher = hashlib.md5()
    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

# Dictionary to store file hashes
file_hashes = {}

# Function to remove duplicates based on filename patterns like "(1)", "(2)"
def remove_name_based_duplicates(filename):
    # Use regex to detect files with (1), (2) at the end of the name
    base_name = re.sub(r"\(\d+\)", "", filename).strip()
    return base_name

# Traverse the directory tree using os.walk()
for root, dirs, files in os.walk(main_directory):  # root is the current directory, dirs are subdirectories, files are the files in the current directory
    for filename in files:
        file_path = os.path.join(root, filename)

        # Check if it's a file
        if os.path.isfile(file_path):
            extension = os.path.splitext(filename)[1].lower()

            # Move files to corresponding folder based on extension
            if extension in extensions:
                folder_name = extensions[extension]
                folder_path = os.path.join(main_directory, folder_name)  # Organize within the main directory
                os.makedirs(folder_path, exist_ok=True)

                destination_path = os.path.join(folder_path, filename)

                # Check for duplicates by file name pattern first
                base_name = remove_name_based_duplicates(filename)

                # Check for duplicates by file size or hash
                file_hash = calculate_hash(file_path)  # Optional, use for content-based duplicate detection

                # If file with same hash or same base name exists, consider it a duplicate
                if file_hash in file_hashes or base_name in file_hashes:
                    print(f"Duplicate found: {filename}. Deleting duplicate.")
                    os.remove(file_path)  # Delete duplicate
                else:
                    file_hashes[file_hash] = file_path  # Store the file hash and base name
                    file_hashes[base_name] = file_path  # Store base name for future name-based duplicate detection
                    shutil.move(file_path, destination_path)
                    print(f"Moved {filename} to {folder_name} folder.")
            else:
                print(f"Skipped {filename}. Unknown file extension.")
        else:
            print(f"Skipped {filename}. It is a directory.")

print("File organization and duplicate removal completed.")
