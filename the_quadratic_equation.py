import math  

A = float(input('Enter number A\n')) 
B = float(input('Enter number B\n'))
C = float(input('Enter number C\n'))

D = B**2 - 4*A*C
print('D =', D)

if D > 0:  
    x1 = (-B + math.sqrt(D)) / (2*A)
    x2 = (-B - math.sqrt(D)) / (2*A)
    print('x1 =', format(x1, '.2f'))
    print('x2 =', format(x2, '.2f')) 
elif D == 0:  
    print(-B / (2 * A)) 
else:  
    print('No roots')