import os
import shutil

# Folder path (change this to your folder)
path = "C:/Users/Lokes/Downloads"

files = os.listdir(path)

for file in files:
    filename, extension = os.path.splitext(file)

    if extension in [".jpg", ".png"]:
        folder = "Images"
    elif extension in [".pdf", ".docx"]:
        folder = "Documents"
    elif extension in [".mp4", ".mkv"]:
        folder = "Videos"
    else:
        folder = "Others"

    folder_path = os.path.join(path, folder)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    shutil.move(os.path.join(path, file), os.path.join(folder_path, file))

print("Files organized successfully!")