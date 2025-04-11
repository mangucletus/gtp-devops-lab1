import requests
import os
import shutil
from datetime import datetime

# Step 1: Clean up previous directory if exists
download_folder = "cletus_mangu"
if os.path.exists(download_folder):
    try:
        shutil.rmtree(download_folder)
        print(f"Directory '{download_folder}' has been removed successfully.")
    except Exception as e:
        print(f"Error: {e}")

# Step 2: Create new directory
os.makedirs(download_folder)
print(f"Directory: '{download_folder}' created.")

# Step 3: Define local file path
local_file_path = os.path.join(download_folder, "cletus_mangu.txt")

# Step 4: Download the file from GitHub
url = "https://raw.githubusercontent.com/sdg000/pydevops_intro_lab/main/change_me.txt"
response = requests.get(url)

if response.status_code == 200:
    print("File successfully downloaded.")
    with open(local_file_path, "wb") as file:
        file.write(response.content)
    print("File saved successfully.")
else:
    print(f"Failed to download file. Status code: {response.status_code}")
    exit()

# Step 5: Overwrite the file content
user_input = input("Describe what you have learned so far in a sentence: ")
now = datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")

with open(local_file_path, "w") as file:
    file.write(user_input + "\n")
    file.write(f"Last modified on: {current_time}\n")

print("File successfully modified.")

# Step 6: Display updated file content
print("\nYou Entered: ")
with open(local_file_path, "r") as file:
    print(file.read())
