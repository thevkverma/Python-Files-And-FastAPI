li = list(range(1,25))

even_number = []

odd_number = []

for item in li:
    if item % 2 ==0:
        even_number.append(item)
    else:
        odd_number.append(item)    
print("Even numbers are:", even_number)
print("Odd numbers are:", odd_number)        