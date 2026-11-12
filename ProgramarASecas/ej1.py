for i in range(1, 101):
    if i%3 !=0 and i%5 !=0:
        print(i)
    if i%3 == 0:
        print(i,"fizz")
    if i%5 == 0:
        print(i,"buzz")
    if i%3 == 0 and i%5 == 0:
        print(i,"fizzbuzz")