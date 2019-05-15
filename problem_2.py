import os
# os.path.isdir(path)
# os.path.isfile(path)
# os.listdir(directory)
# os.path.join(...)
# Listing Out only directories
# directories = filter(os.path.isdir, os.listdir(os.curdir))

# Listing Out only files in current directory
# files = filter(os.path.isfile, os.listdir(os.curdir))
# list_of_paths = os.listdir("./testdir")
# print('listofpaths', list_of_paths)
# for files in list_of_paths:
#     file_confirmed = os.path.isfile(files)
#     print('file', file_confirmed, suffix)
#     print('files', files)

#     if file_confirmed:
#         print(files.endswith(suffix))
# directories = os.path.join(os.path.isdir, os.listdir(os.curdir))
# directories = [ x for x in os.listdir('.') if os.path.isdir(x) ]
# return [x[0] for x in os.walk(list_of_paths)]
# os.path.isdir(os.path.join(a_dir, name))
# dir_list = next(os.walk('.'))[2]

# print('dirlist', [x[0] for x in os.walk(file_confirmed)])


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


# def find_files(suffix, path): 
#    files_found = [] 
#    recursive_file_search(suffix, path, files_found) 
#    return files_found

# import os
# def get_immediate_subdirectories(a_dir):
#     return [name for name in os.listdir(a_dir)
#             if os.path.isdir(os.path.join(a_dir, name))]