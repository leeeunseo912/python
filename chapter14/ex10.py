import os

def get_file_list(dir_path,ext):
    files = os.listdir(dir_path)
    files = list(filter(lambda name : name.endswitch(ext),files))
    return files
    
DIR_PATH = 'c:/temp/music'
songs = get_file_list(DIR_PATH,'.mp3')

for f in songs:
    print(f'{DIR_PATH}/{f}')
    print(os.path.join(DIR_PATH,f))