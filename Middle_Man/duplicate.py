import shutil
from pathlib import Path

# The source of the file
source_file = Path("keylogger.py")
# duplciated file, originated from the source
destination_file = "backup_keylogger.py"


try:
    # shutil.copyfile, only the content of the file
    # shutil.copy, content and permission of the file
    # shutil.copy2, complete duplication, preserving all the file metadata
    shutil.copy2(source_file, destination_file)

except FileNotFoundError:

    print(f"Error: Source file {source_file} does not exists")
