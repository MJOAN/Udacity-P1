import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix ".c"
    Args: suffix(str): suffix if the file name to be found
    path(str): path of the file system
    Returns: a list of paths
    """
    root_dir = '.'
    for root, directories, files in os.walk(root_dir, topdown=False):
        for file_name in files:
            if file_name.endswith(suffix):
                print(root,  file_name)
            
    return None

find_files('.c', '/Users/mariamjoan/Notebooks/testdir')