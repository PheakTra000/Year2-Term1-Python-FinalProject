from pathlib import Path

# This is the home directory of the user, we need it to combine its path of the user startup folder
home_directory = Path.home()

# The directory of the current script, we want to move
soruce_file = Path("path.py")

# The startup folder of the user
destination_folder = home_directory / 'AppData' / 'Roaming' / 'Microsoft' / 'Windows' / 'Start Menu' / 'Programs' / 'Startup'

# / represent as a path joiner, so this the result of the new path
new_path = destination_folder / soruce_file.name

soruce_file.replace(new_path)
