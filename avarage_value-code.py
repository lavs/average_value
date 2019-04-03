def dictUpdateFunction(strText):
    for key in range(1, 5):     # key - номер столбца в файлах
        list_value = float(strText[key])    #list_value - строка в исходном файле
        dic[key].append(list_value)        #накопление количества строк, необходимого для усреднения

    print('dic: ', dic)
    return dic

numPP = 1        #№ п/п
n = 0           #число усреднения строк
while n <= 1:
        print('Введите число строк больше 1: ', end='')
        n = int(input())

dic = {a: ['-'] for a in range(1, 5)}
work_file = open("D:\\tmp\\outSNGS.txt", "r")     #читаем файл
final_file = open("D:\\tmp\\final_text.txt", "w")   #сюда пишем результат

for i in work_file:
        strText = i.split(';')      #разделяем строку на отдельные значения
        print('Исходные значения: ', strText)
        if i.count('"') < 3:    #заголовки в заключены в "", но "" присутствуют так же в первом столбце - датах
            if numPP >= n:      #усредняем значения и выводим результат
                    i = 0
                    dictUpdateFunction(strText)
                    for key in range(1, 5):
                        dic[key].pop(0)     #удаление строки, входящей в предыдущий диапазон вычислений
                        sumList = 0

                        for i in dic[key]:
                            sumList += float(i)
                            print('sumList', sumList)

                        medium = sumList / n        #среднее значение
                        print('Итог: ', str(medium))
                        final_file.write(str(medium) + '    ') # запись среднего значения в файл

                    final_file.write('\n')   #перевод строки в файле
                    numPP += 1

            else:   #подготовка данных к усреднению, накопление значений в словарь
                    dictUpdateFunction(strText)
                    for key in range(1, 5):
                        print(dic[key][0], end='       ')
                        final_file.write(dic[key][0]) # запись в файл значений по умолчанию, в данном случае это "-"
                    final_file.write('\n')
                    print()
                    numPP += 1  #счётчик строк, взятых в работу с исходного файла
        else:
            final_file.write(''.join(str(n)))
            final_file.write('\n')

work_file.close()   #закрытие рабочего и итогового файлов
final_file.close()
