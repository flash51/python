while True:
    try:
        n = int(input("Please choose a number to divide: "))
        list = [d for d in range(1, n + 1) if n % d == 0]
        print("The divisors of {} are: \n {}".format(n,list)) if len(list) > 2 \
            else: print(str(n) + " is a prime number")
    except ValueError:
        print("Very funny smartass. Now give me a number.")
