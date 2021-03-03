while True: # Выполняем цикл, пока не будет введена команда Exit
    select_color = input ('What is the traffic light signal now?\n')
    if select_color == 'Red':
        print ("Don't walk")
    elif select_color == 'Orange':
        print ('Wait')
    elif select_color == 'Green':
        print ('Go')
    elif select_color == 'Exit': # Команда для выхода из цикла
        print ('GoodBye')
        break            
    else:
        print ("I'm don't know this command")

    