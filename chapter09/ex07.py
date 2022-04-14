nums = [n * 2 for n in range(1,11)]

for i in nums:
    print(i, end= ",")

nums = []
print()
print([n for n in range(1,11) if n%3 ==0])