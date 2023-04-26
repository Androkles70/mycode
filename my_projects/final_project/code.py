#!/usr/bin/env python
"""Alexandra | File Organizer"""

import os
import shutil

# Define the directory to organize
directory = "C:/Users/YourUserName/Downloads"

# Define the folders to move files to based on file type
folders = {
    "Images": [".jpeg", ".jpg", ".png", ".gif"],
    "Documents": [".pdf", ".doc", ".docx", ".txt"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv"],
    "Music": [".mp3", ".wav", ".flac", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar"],
    "Programs": [".exe", ".msi", ".dmg", ".pkg"],
}

# Define the backup directory
backup_directory = "C:/Users/YourUserName/Downloads/Backup"

# Define a function to create a directory if it does not exist
def create_directory(directory):
    if not os.path.exists(directory):
        os.mkdir(directory)

# Define a function to move a file to a folder
def move_file(filename, folder):
    source = os.path.join(directory, filename)
    destination = os.path.join(directory, folder, filename)
    if not os.path.exists(destination):
        shutil.move(source, destination)

# Define a function to backup a file
def backup_file(filename):
    source = os.path.join(directory, filename)
    destination = os.path.join(backup_directory, filename)
    if not os.path.exists(destination):
        shutil.copy2(source, destination)

# Define a function to rename a file with a suffix
def rename_file(filename, suffix):
    basename, extension = os.path.splitext(filename)
    new_filename = f"{basename}_{suffix}{extension}"
    source = os.path.join(directory, filename)
    destination = os.path.join(directory, new_filename)
    os.rename(source, destination)

# Define a function to delete a file
def delete_file(filename):
    source = os.path.join(directory, filename)
    os.remove(source)

# Create the folders if they do not exist
for folder in folders:
    create_directory(os.path.join(directory, folder))

# Backup, rename, and move files to folders based on file type
for filename in os.listdir(directory):
    if os.path.isfile(os.path.join(directory, filename)):
        for folder, extensions in folders.items():
            if any(filename.endswith(extension) for extension in extensions):
                backup_file(filename)
                count = 0
                while os.path.exists(os.path.join(directory, folder, filename)):
                    count += 1
                    suffix = str(count)
                    rename_file(filename, suffix)
                move_file(filename, folder)

# Delete duplicate files
for folder, _, files in os.walk(directory):
    for filename in files:
        filepath = os.path.join(folder, filename)
        if os.path.isfile(filepath):
            with open(filepath, "rb") as f:
                contents = f.read()
            for backup_folder, _, backup_files in os.walk(backup_directory):
                for backup_filename in backup_files:
                    backup_filepath = os.path.join(backup_folder, backup_filename)
                    if os.path.isfile(backup_filepath):
                        with open(backup_filepath, "rb") as f:
                            backup_contents = f.read()
                        if contents == backup_contents:
                            delete_file(filepath)

