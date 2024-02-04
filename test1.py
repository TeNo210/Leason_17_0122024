numbers=[1,2,3,4,5]
result = []
for number in numbers:
    if number > 3 and number < 10:
        result.append(number)
print(result)
result1 = [number for number in numbers if number > 3 and number < 10]
print(result1)

