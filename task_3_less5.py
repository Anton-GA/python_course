def sum_in_bank(summ,percent,period):
    """ Калькулятор вклада

    summ -- сумма первоначального взноса
    percent -- процентная ставка
    period -- срок накоплений
    """
    for i in range (period):
        summ += summ / 100*percent
    return summ

summ = eval(input())
percent = eval(input())
period = eval(input())
print(sum_in_bank(summ,percent,period))