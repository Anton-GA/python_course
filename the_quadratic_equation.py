import math # Импортируем, чтобы использовать sqrt
A = float(input ('Enter number A\n')) 
B = float(input ('Enter number B\n'))
C = float(input ('Enter number C\n'))

D = B**2 - 4 * A * C
print ('D =', D)

if D > 0: # Если дискриминант > 0 => имеется два корня
    x1 = (-B + math.sqrt(D)) / (2 * A)
    x2 = (-B - math.sqrt(D)) / (2 * A)
    print ('x1 =', format(x1, '.2f'))
    print ('x2 =', format(x2, '.2f')) 
elif D == 0: #Если дискриминант равняется нулю
    print (-B / (2 * A)) #Только один корень
else: # Если дискриминант меньше нуля, то корней нет
    print ('No roots')