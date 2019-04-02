def dictUpdateFunction(strText):
    lisText = []
    for key in range(1, 5):
            list_key = int(key)                      #   ключ для словаря значений
            list_value = float(strText[key])          #   тут значение для словаря
            dic[list_key].append(list_value)        #   добавление значения в словарь
            dic[list_key].pop(0)
            sumList = 0

            for i in dic[list_key]:
                sumList += float(i)
                print('sumList', sumList)
            lisText.append(str(sumList / n))
            print('lisText', lisText)

    print('Итог: ', lisText)

    return lisText

"---------------------------------------------------"

numPP = 1        #№ п/п
n = 0           #число усреднения строк
while n <= 1:
        print('Введите число строк больше 1: ', end='')
        n = int(input())

dic = {a: ['-'] for a in range(1, 5)}


work_file = open("D:\\tmp\\outSNGS.txt", "r")     #читаем файл
#work_file = open("D:\\tmp\\text_test.txt", "r")     #читаем файл
final_file = open("D:\\tmp\\final_text.txt", "w")   #сюда пишем результат

for i in work_file:
        strText = i.split(';')      #разделяем строку на отдельные значения
        print('Исходные значения: ', strText)
        if i.count('"') < 3:    #заголовки в заключены в "", но "" присутствуют так же в первом столбце - датах
            if numPP >= n:      #усредняем значения и выводим результат

                    i = 0
                    final_file.write('    '.join(dictUpdateFunction(strText)))
                    final_file.write('\n')
                    numPP += 1
            else:       #подготовка данных к усреднению
                    for key in range(1, 5):
                            list_key = int(key)                      #   ключ для словаря значений
                            list_value = float(strText[key])          #   тут значение для ключа
                            dic[list_key].append(list_value)        #   добавление значения в словарь
                            print(dic[list_key][0], end='       ')
                            final_file.write(dic[list_key][0])
                    final_file.write('\n')

                    print()
                    numPP += 1
        else:
            final_file.write(''.join(str(n)))
            final_file.write('\n')

work_file.close()
final_file.close()
