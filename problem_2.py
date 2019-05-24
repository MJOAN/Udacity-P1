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
                print(os.path.join(root, file_name))
            
    return None

# Test Case 1 
find_files('.c', '/Users/mariamjoan/Notebooks/testdir')
# ./testdir/subdir3/subsubdir1 b.c
# ./testdir/subdir5 a.c
# ./testdir/subdir1 a.c
# ./testdir t1.c


# Test Case 2
find_files('.h', '/Users/mariamjoan/Notebooks/testdir')
# ./testdir/subdir3/subsubdir1 b.h
# ./testdir/subdir5 a.h
# ./testdir/subdir1 a.h
# ./testdir t1.h


# Test Case 3
find_files('.', '/Users/mariamjoan/Notebooks/testdir')
# ./testdir/subdir3/subsubdir1 b.h
# ./testdir/subdir5 a.h
# ./testdir/subdir1 a.h
# ./testdir t1.h