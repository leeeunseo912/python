import pickle
import json
import os

def save(file_name, data):
    try:
        with open(file_name, 'wb') as file:
            pickle.dump(data,file)
    except Exception as e:
        print(e)
def load(file_name):
    try:
        with open(file_name, 'rb') as file:
            data = pickle.load(file)
            return data

    except Exception as e:
        print(e)

def save_json(file_name, data):
    try:
        with open(file_name, 'wt') as file:
            json.dump(data,file)
    except Exception as e:
        print(e)

def load_json(file_name):
    try:
        with open(file_name, 'rt') as file:
            data = json.load(file)
            return data

    except Exception as e:
        print(e)



def get_file_list(dir_path,ext):
    files = os.listdir(dir_path)
    files = list(filter(lambda name: name.endswith(ext),files))

    return files