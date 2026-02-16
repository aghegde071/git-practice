num = 7  # Fixed value for CI testing

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is NOT a Prime Number")
            break
    else:
        print(num, "is a Prime Number")
else:
    print(num, "is NOT a Prime Number")

