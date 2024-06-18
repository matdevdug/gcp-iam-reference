import os
import json
import unittest

class TestRolesDirectory(unittest.TestCase):

    def test_json_files_in_roles_directory(self):
        roles_directory = '../roles'

        # Ensure the 'roles' directory exists
        self.assertTrue(os.path.exists(roles_directory) and os.path.isdir(roles_directory))

        # Get a list of files in the 'roles' directory
        files = [f for f in os.listdir(roles_directory) if os.path.isfile(os.path.join(roles_directory, f))]

        # Ensure there is at least one file in the 'roles' directory
        self.assertGreater(len(files), 0, "No files found in the 'roles' directory")

        for file_name in files:
            # Ensure the file name has the format word.word
            self.assertTrue(len(file_name.split('.')) == 2, f"Invalid file name format: {file_name}")

            # Check if the JSON file is not empty
            file_path = os.path.join(roles_directory, file_name)
            with open(file_path, 'r') as file:
                json_data = json.load(file)
                self.assertGreater(len(json_data), 0, f"JSON file is empty: {file_name}")

if __name__ == '__main__':
    unittest.main()
