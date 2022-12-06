def (listX:list, listP:list):


def FillList(listX:list, listP:list):
    while True:
        print(f'Введите значения по X:')
        for line in iter(input, ''):
            listX.append(float(line))
        if len(listX) < 1:
            print("не введено не одного значения")
            continue
        break
    print(str(len(listX)) +" значений в таблице\n"
                            "введите значениея P:")
    i = 0
    while i < len(listX):
        listP.append(float(input(str(i+1) + ": ")))
        i+=1
        continue
    return

def Main():
    listX1 = []
    listP1 = []
    print("Ввод первой таблицы:")
    FillList(listX1, listP1)

    listX2 = []
    listP2 = []
    print("\nВвод второй таблицы:")
    FillList(listX2, listP2)


    return 0

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Main()

