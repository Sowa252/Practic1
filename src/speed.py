import math

def speed_object(d):
    Vi=0
    const_a=9.8
    return math.sqrt(Vi**2+2*const_a*d)

def run():
    try:
        print("Расчета скорости объекта во время его соприкосновения с землей")
        inp1=input("Введите высоту:")
        inp1 = float(inp1)
        if inp1 <= 0:
            print("Число должно быть больше 0")
            return
        ret = speed_object(inp1)
        print("Результат: {} м/с".format(ret))
    except ValueError as err:
        print("Ошибка: {}".format(str(err)))
        return str(err)

if __name__=="__main__":
    run()
