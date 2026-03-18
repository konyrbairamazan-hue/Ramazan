import shutil
import os

# Copying: shutil.copy(source, destination) creates a duplicate of the file
shutil.copy('output.txt', 'copy_output.txt')

# Deleting: First, we check if the file exists to avoid a crash
if os.path.exists('copy_output.txt'):
    # os.remove() permanently deletes the specified file
    os.remove('copy_output.txt')
    print("File deleted successfully")