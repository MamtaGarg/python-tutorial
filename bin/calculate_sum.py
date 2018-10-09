import re
handle = open("../regex_sum.txt")
numbers = []
for line in handle:
        words = line.strip().split()
        for word in words:
            temp = re.findall(r'\d+',word)
            if len(temp) !=0:
                numbers.append(temp)
print(numbers)
sum = 0
for num in numbers:
    for value in num:
        sum += int(value)
print(sum)
