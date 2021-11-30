import sys
import time
from speed import speed_object
from square import calculation_of_square

# Декоратор расчитывает время выполнения функции и выводит ее имя
def runtime(func):
    def wrapper(*arg1):
        start = time.time()
        ret = func(*arg1)
        end = time.time()
        print('Время выполнения: {} секунд.'.format(end-start))
        print('Выполненая функция: {}'.format(func))
        return ret
    return wrapper

#Функция расчета площади
@runtime
def soft_per_acre(L,M):
    return calculation_of_square(L,M)

# функция расчета скорости    
@runtime
def svob_pad(d):    
    return speed_object(d)

def main():
    try:
        print("Если вы введете 2 числа, то посчитается площадь участка, если одно число то скорость свободного падения")
        inp1=input("Введите 1 число:")
        inp2=input("Введите 2 число /(или нажмите Enter/):")
        inp1 = float(inp1)
        if inp1 < 0:
            print("Введенное значение должно быть больше 0")
            return
        if inp2 != "" :
            inp2 = float(inp2)
            if inp2 < 0:
                print("Введенное значение должно быть больше 0")
                return
            ret = soft_per_acre(inp1, inp2)
            ret1 = "акров"
        else :
            ret = svob_pad(inp1)
            ret1 = "м/с"
        print("Результат: {} {}".format(ret, ret1))
    except ValueError as err:
        print("Ошибка: {}".format(str(err)))
        return str(err)

main()
