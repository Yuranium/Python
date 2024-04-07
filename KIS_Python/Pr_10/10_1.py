def transform_table(input_table):
    cleaned_table = [list(filter(None, row)) for row in input_table]
    unique_rows = []
    [unique_rows.append(row) for row in cleaned_table if row not in unique_rows]
    final_table = list(filter(None, unique_rows))

    for i, row in enumerate(final_table):
        if ':' in row[0]:
            final_table[i][0], email = row[0].split(':')
            final_table[i].insert(1, email.split('@')[0])

    transformed_data = []
    for row in final_table:
        if len(row) >= 3:
            date, percentage, email = row
            formatted_date = '/'.join(date.split('/')[::-1])
            phone_number = ''.join(filter(str.isdigit, email))
            percentage = f"{int(float(percentage) * 100)}%"
            username = email.split('@')[0]
            transformed_data.append(['+' + phone_number, percentage, formatted_date, username])

    return transformed_data

# Пример входных данных (замените на свои)
input_data = [
    ["1999/10/05:+7", "0.8", "siduskol0@yandex.ru"],
    ["1999/10/16:+7", "0.1", "salolin23@gmail.com"],
    ["1999/08/05:+7", "0.9", "timofej97@yahoo.com"],
    ["1999/08/05:+7", "0.9", "timofej97@yahoo.com"]
]

transformed_data = transform_table(input_data)
print(transformed_data)
