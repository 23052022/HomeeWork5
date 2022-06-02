number = input("...")
sum = 0
count = 0
max = 0
min = None
while True:
    s = input("enter: ")
    if not s:
       print(sum, count,max, min, mean)
       break
    number = int(s)
    sum +=number
    count += 1
    if number > max:
        max = number
    if min is None or number < min:
        min = number
    mean = sum/count

