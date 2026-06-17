
# Handles loading and managing data from the filesystem.


import os
from app.parser.txt_parser import parse_txt


class DataService:
  
# Central service responsible for loading character data from files.
  
    def __init__(self):
        self.folder_path = None
        self.characters = []

    def set_folder(self, path):
  
# Sets the directory where character files are located.
  
        self.folder_path = path
        self.load_data()

    def load_data(self):
 
# Loads all character files from the selected directory.
 
        self.characters = []

        if not self.folder_path:
            return

        for file in os.listdir(self.folder_path):
            if file.endswith(".txt"):
                full_path = os.path.join(self.folder_path, file)
                character = parse_txt(full_path)
                self.characters.append(character)

    def get_characters(self):
        return self.characters