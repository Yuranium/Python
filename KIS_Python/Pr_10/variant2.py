def process_row(row):
    un = row[0].split(';')[0]
    name = row[0].split(';')[1].split('/')[::-1]
    formatted_name = "/".join(name)
    status = "Выполнено" if row[1] == "Да" else "Не выполнено"
    second_word = un.split()[1]
    email = row[3].split('@')[0]
    return [formatted_name, status, second_word, email]


def main(input_table):
    seen_names = set()
    unique_rows = []
    for row in input_table:
        if all(row) and None not in row:
            name = row[0].split(';')[0]
            if name not in seen_names:
                unique_rows.append(process_row(row))
                seen_names.add(name)

    return unique_rows

# Пример использования
input_table = [
    ["Макар Каманов;00/01/24", "Да", "kamanov78@mail.ru", "kamanov78@mail.ru"],
    ["Макар Каманов;00/01/24", "Да", "kamanov78@mail.ru", "kamanov78@mail.ru"],
    ["Тихон Бидиди;02/01/19", "Да", "bididi88@gmail.com", "bididi88@gmail.com"],
    [None, None, None, None],
    ["Руслан Лобли;03/04/25", "Нет", "ruslan90@yandex.ru", "ruslan90@yandex.ru"],
    [None, None, None, None],
    ["Вадим Суфимянц;04/11/25", "Да", "sufimanz9@mail.ru", "sufimanz9@mail.ru"]
]

result_table = main(input_table)

# Вывод результата
for row in result_table:
    print('\t'.join(row))
