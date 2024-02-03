import csv


def gen_password(dict_sh):
    """
    dict_sh - словарь, который был получен с помощью DictReader-а:
    возвращается сгенерированный по данному условию пароль:
    """
    planet_letters = dict_sh['planet'][-3:-1]
    two_central_letters = dict_sh['ShipName'][2] + dict_sh["ShipName"][1]
    three_letters = dict_sh['planet'][2] + dict_sh['planet'][1] + dict_sh['planet'][0]
    password = planet_letters.upper() + two_central_letters.upper() + three_letters.upper()
    return password


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
    with open('space.csv') as f_our:
        with open('space_uniq_password.csv', 'w') as final_file:
            writer = csv.DictWriter(final_file, fieldnames=fieldnames + ['password'])  # Создание объекста dictwrier
            writer.writeheader()  # запись заголовков
            dict_reader = csv.DictReader(f_our, fieldnames=fieldnames)

            # заполнение writer-а на основе dict_reader-а
            for d in dict_reader:
                pas = gen_password(d)
                writer.writerow(dict(zip(fieldnames + ['password'], [d['ShipName'], d['planet'], d['coord_place'],
                                                                     d['direction'], pas])))
