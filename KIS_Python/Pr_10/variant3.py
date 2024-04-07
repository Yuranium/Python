def main4(row, unique_transformed_data):
    transformed_row = []
    for cell in row:
        if cell is None:
            continue
        transformed_row = main2(cell, transformed_row)
    transformed_row[1], transformed_row[2] = (
        transformed_row[2], transformed_row[1])
    unique_transformed_data = main3(transformed_row,
                                    unique_transformed_data)
    return unique_transformed_data


def main3(transformed_row, unique_transformed_data):
    unique_transformed_data[tuple(transformed_row)] = transformed_row
    return unique_transformed_data


def main2(cell, transformed_row):
    if '(' in cell:
        phone_parts = [char for char in cell[11:29] if char.isdigit()]
        phone = ''.join(phone_parts)
        transformed_row.append(f"+{phone}")
    if cell.replace('.', '').isdigit():
        percent = int(float(cell) * 100)
        transformed_row.append(f"{percent}%")
    if cell.count('/') == 2:
        date_parts = cell.split('/')
        day, month, year = (date_parts[2].split(':')[0],
                            date_parts[1], date_parts[0])
        transformed_row.append(f"{day}/{month}/{year}")
    if '@' in cell:
        email_parts = cell.split('@')
        transformed_row.append(email_parts[0])
    return transformed_row


def main(input_data):
    unique_transformed_data = {}
    for row in input_data:
        if row.count(None) == len(row):
            continue
        unique_transformed_data = main4(row,
                                        unique_transformed_data)
    return list(unique_transformed_data.values())

# Пример использования
# input_data = [
#     ["1999/10/05:+7 (573) 048-59-03", "0.8", None, "siduskol0@yandex.ru"],
#     ["1999/10/16:+7 (995) 153-30-76", "0.1", None, "salolin23@gmail.com"],
#     ["1999/08/05:+7 (171) 185-12-70", "0.9", None, "timofej97@yahoo.com"],
#     ["1999/08/05:+7 (171) 185-12-70", "0.9", None, "timofej97@yahoo.com"]
# ]
input_data = [[None, None, None, None, None],
              [None, '2004/09/18:+7 (250) 086-81-28', '0.3', None, 'odissej73@yandex.ru'],
              [None, '2000/07/26:+7 (449) 308-81-56', '1.0', None, 'lozan38@mail.ru'],
              [None, '2001/06/12:+7 (374) 734-86-17', '0.2', None, 'al_bert41@yandex.ru'],
              [None, None, None, None, None],
              [None, '2004/11/27:+7 (638) 495-90-90', '0.6', None, 'fizokin3@gmail.com'],
              [None, '2004/11/27:+7 (638) 495-90-90', '0.6', None, 'fizokin3@gmail.com']]
output_data = main(input_data)
print(output_data)
