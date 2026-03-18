import os
# Create a new directory; 'exist_ok=True' prevents an error if the folder already exists
os.makedirs('new_folder', exist_ok=True)
# Get a list of all files and folders in the current directory ('.')
files = os.listdir('.')
# Print the list of files to the console
print("List of files:", files)