import csv

with open('space.txt') as file:
    data = list(map(lambda el: el.strip().split('*'), file.readlines()))
    fieldnames = data[0]

    # подготовка файла csv для упрощения задачи
    with open('space.csv', 'w') as extra_file:
        dict_writer = csv.DictWriter(extra_file, fieldnames=fieldnames)  # создание объекта dictwriter

        # наполнение dict_writer информацией из space.txt
        for el in data[1:]:
            dict_writer.writerow(dict(zip(fieldnames, el)))

    # открытие созданного нами файла space.csv
    with open('space.csv') as f:
        dict_reader = csv.DictReader(f, fieldnames=fieldnames)

        # начало цикла по выдаче информации о корабле
        st = input()
        while st != 'stop':
            flag_error = True  # флаг, который показывает, был ли найден корабль по имени. Если нет - печатается error
            for d in dict_reader:  # проход по словарям в dict_reader
                if d['ShipName'] == st:
                    print(f'Корабль {d["ShipName"]} был отправлен с планеты: {d["planet"]}'
                          f'и его направление движения было: {d["direction"]}')
                    flag_error = False
            if flag_error:
                print('error.. er.. ror..')
            st = input()
            f.seek(0)  # установка курсора в начало файла, так как при проходе по словорям в dict_reader
            # позиция курсора стала последней
