import re
from os import listdir, path
from os.path import isfile, join

ADDITIONAL_FILES_DIR_NAME = 'additions'
ADDITIONAL_FILE_SUFFIX = ' - נספח'


class FileManager:

    def __init__(self, base_dir):
        self.base_dir = base_dir
        self.files = [f for f in listdir(base_dir) if not re.search("xml", f) and isfile(join(base_dir, f))]

        additional_files_dir = path.join(base_dir, ADDITIONAL_FILES_DIR_NAME)
        self.files += [f + ADDITIONAL_FILE_SUFFIX for f in listdir(additional_files_dir) if isfile(join(additional_files_dir, f))]

    def find_optional_matches(self, search_input):
        return [] if search_input == '' else [f for f in self.files if re.search(search_input, f.replace('.txt', ''))]

    def find_optional_matches_by_prefix(self, prefix):
        return [] if prefix == '' else [f for f in self.files if f.startswith(prefix)]

    def read_file(self, file_name):
        file_name = file_name.replace(ADDITIONAL_FILE_SUFFIX, '')
        try:
            f = open(path.join(self.base_dir, file_name), "r", encoding="utf8")
            return f.read()
        except FileNotFoundError:
            pass

        try:
            f = open(path.join(self.base_dir, ADDITIONAL_FILES_DIR_NAME, file_name), "r", encoding="utf8")
            return f.read()
        except FileNotFoundError:
            print('Error: could not find ' + file_name)

