def process_row(row):
    if len(row) == 5:  # Старый формат данных
        un = (row[1].split(':')[1].replace('(', '').replace(')', '')
              .replace('-', '').replace(' ', ''))
        percentage = str(int(float(row[2]) * 100)) + '%'
        date = row[1].split(':')[0].split('/')[::-1]
        formatted_date = "/".join(date)
        username = row[4].split('@')[0].split('.')[0]
    elif len(row) == 4:  # Новый формат данных
        un = (row[0].split(':')[1].replace('(', '').replace(')', '')
              .replace('-', '').replace(' ', ''))
        percentage = str(int(float(row[1]) * 100)) + '%'
        date = row[0].split(':')[0].split('/')[::-1]
        formatted_date = "/".join(date)
        username = row[3].split('@')[0].split('.')[0]
    return [un, percentage, formatted_date, username]


def extract_date(row):
    if len(row) == 5:
        return row[1].split(':')[0]
    elif len(row) == 4:
        return row[0].split(':')[0]


def is_valid_row(row):
    if len(row) == 5:
        return row[1] and row[2] and row[4]
    elif len(row) == 4:
        return row[0] and row[1] and row[3]


def main(input_data):
    seen_dates = set()
    unique_rows = []
    for row in input_data:
        if is_valid_row(row):
            date = extract_date(row)
            if date not in seen_dates:
                unique_rows.append(process_row(row))
                seen_dates.add(date)
    return unique_rows


# Пример использования с новыми данными
input_data = [
    ["1999/10/05:+7 (573) 048-59-03", "0.8", None, "siduskol0@yandex.ru"],
    ["1999/10/16:+7 (995) 153-30-76", "0.1", None, "salolin23@gmail.com"],
    ["1999/08/05:+7 (171) 185-12-70", "0.9", None, "timofej97@yahoo.com"],
    ["1999/08/05:+7 (171) 185-12-70", "0.9", None, "timofej97@yahoo.com"]
]

result_data = main(input_data)
print(result_data)

# Пример использования с предыдущими данными
input_data_old = [
    [None, None, None, None, None],
    [None, '2004/09/18:+7 (250) 086-81-28', '0.3', None, 'odissej73@yandex.ru'],
    [None, '2000/07/26:+7 (449) 308-81-56', '1.0', None, 'lozan38@mail.ru'],
    [None, '2001/06/12:+7 (374) 734-86-17', '0.2', None, 'al_bert41@yandex.ru'],
    [None, None, None, None, None],
    [None, '2004/11/27:+7 (638) 495-90-90', '0.6', None, 'fizokin3@gmail.com'],
    [None, '2004/11/27:+7 (638) 495-90-90', '0.6', None, 'fizokin3@gmail.com']
]

result_data_old = main(input_data_old)
print(result_data_old)
