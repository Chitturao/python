numbers=[2,2,4,3,6,5,1,5]
unique=[]
for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)