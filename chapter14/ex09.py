from file_util import load, load_json, save, save_json

def main():
    # datas = [123,45,67,89]
    datas =[
        {"name" : "이은서",
        "age" : "25"},
        {"name" : "이홍령",
        "age" : "22"},

    ]

    
    save_json("data1.json",datas)
    content = load_json("data1.json")
    print(content)

main()