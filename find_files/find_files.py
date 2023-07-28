"""find all files within the given path
    Args:
        suffix: str
        path: str
    Returns:
        list: list with full paths
"""

import argparse
import fnmatch
import os


def find_files(suffix, path):    
    list_of_files = os.listdir(path)
    result = []
 
    for entry in list_of_files:        
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            result = result + find_files(suffix, full_path)
        else:
            # fnmatch lib - Unix filename pattern matching
            # more at https://docs.python.org/3/library/fnmatch.html
            if fnmatch.fnmatch(full_path, suffix):                
                result.append(full_path)
                
    return result



if __name__ == "__main__":    
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", type=str, help="suffix of the files to find", required=True)
    parser.add_argument("-p", type=str, help="base path to search for the files", required=True)
    args = parser.parse_args()


    files = find_files(args.s, args.p)
    for file in files:
        print(file)

# print(find_files("*.jpeg", "/Users/tsandesfernandes/Downloads/"))