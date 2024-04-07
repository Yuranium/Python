from collections import OrderedDict


def transform_data(row):
    if row is None:
        return None

    row = [item for item in row if item is not None]
    if len(row) < 3:
        return None

    date, percentage, email = row
    year, month, day = date.split('/')
    formatted_date = f"{day[:2]}/{month}/{year}"

    phone_number = '+' + ''.join(filter(str.isdigit, date[10:]))
    percentage = str(int(float(percentage) * 100)) + "%"
    username = email.split('@')[0]

    return [phone_number, percentage, formatted_date, username]


def main(input_data):
    transformed_data = []

    for row in input_data:
        transformed_row = transform_data(row)
        if transformed_row is not None:
            transformed_data.append(transformed_row)

    res = OrderedDict((tuple(element), element) for element
                      in transformed_data)
    return list(res.values())


input_data = [
    ["1999/10/05:+7 (573) 048-59-03", "0.8", None, "siduskol0@yandex.ru"],
    ["1999/10/16:+7 (995) 153-30-76", "0.1", None, "salolin23@gmail.com"],
    ["1999/08/05:+7 (171) 185-12-70", "0.9", None, "timofej97@yahoo.com"],
    ["1999/08/05:+7 (171) 185-12-70", "0.9", None, "timofej97@yahoo.com"]
]
# input_data = [[None, None, None, None, None],
#               [None, '2004/09/18:+7 (250) 086-81-28', '0.3', None, 'odissej73@yandex.ru'],
#               [None, '2000/07/26:+7 (449) 308-81-56', '1.0', None, 'lozan38@mail.ru'],
#               [None, '2001/06/12:+7 (374) 734-86-17', '0.2', None, 'al_bert41@yandex.ru'],
#               [None, None, None, None, None],
#               [None, '2004/11/27:+7 (638) 495-90-90', '0.6', None, 'fizokin3@gmail.com'],
#               [None, '2004/11/27:+7 (638) 495-90-90', '0.6', None, 'fizokin3@gmail.com']]

output_data = main(input_data)
print(output_data)
