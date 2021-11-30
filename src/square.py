def calculation_of_square(L, M):
    return (M*L)/43560

def run():
    try:
        print("Расчет площади участка в акрах")
        inp1=input("Введите длинну участка в фунтах:")
        inp2=input("Введите ширину участка в фунтах:")
        inp1 = float(inp1)
        inp2 = float(inp2)
        if inp1 <= 0 or inp2 <= 0:
            print("Число должно быть больше 0")
            return
        ret = calculation_of_square(inp1, inp2)
        print("Результат: {} акров".format(ret))
    except ValueError as err:
        print("Ошибка: {}".format(str(err)))
        return str(err)

if __name__=="__main__":
    run()
