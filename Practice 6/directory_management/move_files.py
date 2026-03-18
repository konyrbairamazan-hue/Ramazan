import shutil
import os
# os.path.exists checks if the file actually exists before we try to move it
if os.path.exists('output.txt'):
    # shutil.move(source, destination) moves and can also rename the file
    shutil.move('output.txt', 'new_folder/moved_output.txt')