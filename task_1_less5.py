# Вычисление факториала
def fact(x: int):  
    if x < 0:
        raise ValueError('x < 0')
    
    if x == 1 or x == 0:
        return 1
    else:
        return x * fact(x-1)

while True:    
    try:
        x = int(input('Enter a number: '))
        x = fact(x)
    except:
        print('Error. Enter again: \n')
        continue
    
    print(x)
    break
