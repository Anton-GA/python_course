function = input('Enter: Simple, GCD, LCM, Stop\n')

while function != 'Stop':
    if function == 'Simple':
        n = int(input('Enter a number\n'))
        k = 0
        for a in range (2, n // 2 + 1):
            if (n % a == 0):
                k = k + 1
        if (k <= 0):
            print("It's a prime number")
        else:
            print("It isn't a prime number")
        function = input('Enter: Simple, GCD, LCM, Stop\n')
    elif function == 'GCD':
        x = int(input('Enter a number\n'))
        y = int(input('Enter a number\n'))
        while x != 0 and y != 0:
            if x > y:
                x %= y
            else:
                y %= x
        result = x + y
        print ('Result: ', result)
        function = input('Enter: Simple, GCD, LCM, Stop\n')
    elif function == 'LCM':
        x = int(input('Enter a number\n'))
        y = int(input('Enter a number\n'))
        z = x * y
        while x != 0 and y != 0:
            if x > y:
                x %= y
            else:
                y %= x
        print ('Result: ', z // (x + y))
        function = input('Enter: Simple, GCD, LCM, Stop\n')
    elif function == 'Stop':
        print ('Goodbye')
        break 
    else:
        print ("I have paws. Sorry((")
        break