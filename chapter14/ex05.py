f = open("live.txt","rt",encoding="utf-8")

f.seek(16,0)
text = f.readline()

f.close()
print(text)