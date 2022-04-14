def seqgen(data):
    for index in range(0,len(data),2):
        yield data[index:index+2]

solar = seqgen("입춘우수경칩춘분청명곡우입하소만망종하지소서대서")
print(solar)

for k in solar:
    print(k, end=",")
