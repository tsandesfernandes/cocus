import tempfile
import os

from find_files import find_files

temp_dir = tempfile.TemporaryDirectory()
dir_path = temp_dir.name
files = [
    os.path.join(dir_path, "file.txt"),
    os.path.join(dir_path, "a", "file1.txt"),
    os.path.join(dir_path, "b", "file2.txt")
]

os.makedirs(os.path.join(dir_path, "a"))
os.makedirs(os.path.join(dir_path, "b"))

for file in files:
    with open(file, "w") as f:
        f.write("file file")


def test_ok():
    result = find_files("*.txt", dir_path)
    expected = [
        os.path.join(dir_path, "file.txt"),
        os.path.join(dir_path, "a", "file1.txt"),
        os.path.join(dir_path, "b", "file2.txt")
    ]


    assert result == expected

def test_ok_empty():
    result = find_files("*.pdf", dir_path)
    expected = [      ]


    assert result == expected


def test_ok_no_suffix():
    result = find_files("", "./")
    expected = []

    assert result == expected