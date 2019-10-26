# Move files to archive

import os

def move_to_archive(path_1, path_2):
    os.chdir(path_1)
    print(os.getcwd())
    get_files = os.listdir()
    os.chdir('..')
    
    for text_file_name in get_files:
        os.rename(str(path_1)+'/'+str(text_file_name),
                  str(path_2)+'/'+str(text_file_name))


