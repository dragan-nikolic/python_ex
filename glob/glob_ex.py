import glob
import os

def test_glob(files_pattern):
    print(f'=== glob files_pattern: {files_pattern}')
    files = glob.glob(files_pattern)
    for f in files:
        if os.path.exists(f):
            #print(f'{f} exists')
            if os.path.isfile(f):
                print(f'{f} is a file')
            elif os.path.isdir(f):
                print(f'{f} is a directory')
            else:
                print(f'{f} is something else')
        else:
            print(f'{f} does not exist')    

test_glob('dir1/f*.txt')
test_glob('dir1/file1.txt')