def file_read(file_name):
    try:
        with open(file_name,'rt', encoding="utf-8") as file:
            text = file.read()
            return text

    except:
        return ''
    

def save(file_name, content):
    with open(file_name, 'wt', encoding='utf-8') as file:
        file.write(content)


def main():
    try:
        file_name = "live.txt"
        text = file_read(file_name)
        print(text)

        new_text = input("추가할 문자열을 입력하시오: ")
        text += new_text + "\n"

        save(file_name,text)
    except Exception as e:
        print(e)

main()
