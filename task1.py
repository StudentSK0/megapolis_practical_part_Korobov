with open('space.txt') as file:
    # чтение исходного файла. Удаление нечитаемых символов и разбиение строки по символу '*':
    data = list(map(lambda el: el.strip().split('*'), file.readlines()))

    # создание 'говорящих' переменных, которые хранят в себе индексы, отвечающие за заголовки
    coord_ind, ship_ind, planet_ind, direct_ind = data[0].index('coord_place'), data[0].index('ShipName'),\
                                                  data[0].index('planet'), data[0].index('direction')
    # открытие файла для записи
    with open('space_new.txt', 'w') as out_file:
        out_file.write('*'.join(['ShipName', 'planet', 'coord_place', 'direction']))  # запись заголовков
        out_file.write('\n')  # переход на новую строку
        for lst in data[1:]:
            if lst[coord_ind] == '0 0':
                n = int(lst[ship_ind].split('-')[-1][0])  # первая цифра в номере корабля
                xd, yd = list(map(int, lst[direct_ind].split(' ')))  # целочисленные координаты направления
                t = len(lst[planet_ind])  # количество букв в родной планете корабля
                m = int(lst[ship_ind].split('-')[-1][1])  # вторая цифра в номере корабля

                # вычисление х и у в соответсвии с условием:
                if n > 5:
                    x = n + xd
                else:
                    x = -1 * (n + xd) * 4 + t
                if m > 3:
                    y = m + t + yd
                else:
                    y = -1 * (n + yd) * m

                # запись строки с найденными х и у в файл space_new.txt:
                out_file.write('*'.join([lst[ship_ind], lst[planet_ind], f'{x} {y}', lst[direct_ind]]))
                out_file.write('\n')
            out_file.write('*'.join([lst[ship_ind], lst[planet_ind], lst[coord_ind], lst[direct_ind]]))
            out_file.write('\n')

            # вывод кораблей, последний элемент кода которых равен 'V'
            if lst[ship_ind].split('-')[0][-1] == 'V':
                print(lst)
