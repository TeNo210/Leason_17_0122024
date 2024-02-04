import random

numbers = [1,2,3,4,5,6,7,8,100]
result = []
for number in numbers:
    if number > 5 and number < 50:
        result.append(number)
print(result)
#filter
result = filter(lambda number:number > 5 and number < 50, numbers)
print(list(result))
#генератор списка
#[элемент <цикл for > if <условие
result1 = [number for number in numbers if number > 5 and number < 50]
print(result1)

names = ['leo','max','kate','mag']

names_upper = [name.upper() for name in names]
print(names_upper)

names_m = [name for name in names if name [0]=='m']
print(names_m)

result01 = [1 if number >5 else 0 for number in numbers]
print(result01)

result011 = {random.randint(a=1,b=10)for i in range (10)}
print(result011)

result012 = {i:i**2 for i in range(1,10)}
print(result012)