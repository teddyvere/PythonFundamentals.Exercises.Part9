import unittest
import json
import os
import pickle
from pathlib import Path
import tempfile
import shutil
import json_helper

# Assuming the functions are imported from your module, e.g.,
# from your_module import read_json, read_all_json_files, write_pickle, load_pickle

class TestJsonFunctions(unittest.TestCase):

    def setUp(self):
        """Create a temporary directory with sample JSON files for testing."""
        self.test_dir = tempfile.mkdtemp()
        self.json_files = {
            'file1.json': {'name': 'Mario', 'game': 'Super Mario'},
            'file2.json': {'name': 'Link', 'game': 'The Legend of Zelda'}
        }

        for filename, content in self.json_files.items():
            with open(os.path.join(self.test_dir, filename), 'w') as f:
                json.dump(content, f)

        self.pickle_file = os.path.join(self.test_dir, 'super_smash_characters.pickle')

    def tearDown(self):
        """Remove the temporary directory and its contents after testing."""
        shutil.rmtree(self.test_dir)

    def test_read_json(self):
        """Test reading a single JSON file."""
        file_path = os.path.join(self.test_dir, 'file1.json')
        expected = self.json_files['file1.json']
        result = json_helper.read_json(file_path)
        self.assertEqual(result, expected)

    def test_read_all_json_files(self):
        """Test reading all JSON files in a directory."""
        result = json_helper.read_all_json_files(self.test_dir)
        expected = list(self.json_files.values())
        self.assertEqual(result, expected)

    def test_write_pickle(self):
        """Test writing JSON objects to a pickle file."""
        json_helper.write_pickle(self.pickle_file)
        with open(self.pickle_file, 'rb') as f:
            result = pickle.load(f)
        expected = list(self.json_files.values())
        self.assertEqual(result, expected)

    def test_load_pickle(self):
        """Test loading and printing contents of a pickle file."""
        json_helper.write_pickle(self.pickle_file)
        with open(self.pickle_file, 'rb') as f:
            expected = pickle.load(f)

        with unittest.mock.patch('builtins.print') as mocked_print:
            json_helper.load_pickle(self.pickle_file)
            calls = [unittest.mock.call(item) for item in expected]
            mocked_print.assert_has_calls(calls, any_order=True)

if __name__ == '__main__':
    unittest.main()