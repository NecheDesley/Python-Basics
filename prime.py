number = int(input("please enter a number: "))


if number > 1:

    for i in range(2, number):

        if (number % i) == 0:
            print("it isn't a prime") 

            break
    else:
        print("it is a prime")
