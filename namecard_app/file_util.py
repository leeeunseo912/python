import pickle
import json

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