num =1
even_sum = 0
odd_sum = 0

while num <= 100:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num
    num += 1

print("짝수의 합 = ", even_sum)
print("홀수의 합 = ", odd_sum)