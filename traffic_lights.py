# Предложим пользователю ввести цвет светофора
select_color = input ('What is the traffic light signal now?\n')
 
if select_color == 'Red':
    print ("Don't walk")
elif select_color == 'Orange':
    print ('Wait')
elif select_color == 'Green':
    print ('Go')    
else: # Если не введен один из обозначенных сигналов 
    print ("I'm don't know this command")    