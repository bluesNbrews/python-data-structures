import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if suffix == "":
        print("No suffix to search for.")
        return

    if path == "":
        print("No path provided.")
        return

    if os.path.isdir(path):
        #print("This is: {}".format(path))
        for item in os.listdir(path):
            find_files(suffix, os.path.join(path, item))
    if os.path.isfile(path):
        #print("This is: {}".format(path))
        if suffix in os.path.basename(path):
            #print("Found: {}".format(os.path.basename(path)))
            files_found.append(path)

if __name__ == "__main__":

    files_found = []

    # Test case 1 - you will need to change the file path but it is the test directory provided by the course
    find_files(".c","/Users/stevenwilliams/Desktop/python_stuff/P1/testdir")
    print(files_found)
    # Test case 2 
    find_files(".c", "")
    # Test case 3 
    find_files("", "/Users/stevenwilliams/Desktop/python_stuff/P1/testdir")
    '''
    Expected output:
    ['/Users/stevenwilliams/Desktop/python_stuff/P1/testdir/subdir3/subsubdir1/b.c', '/Users/stevenwilliams/Desktop/python_stuff/P1/testdir/t1.c', '/Users/stevenwilliams/Desktop/python_stuff/P1/testdir/subdir5/a.c', '/Users/stevenwilliams/Desktop/python_stuff/P1/testdir/subdir1/a.c']
    No path provided.
    No suffix to search for.
    '''
