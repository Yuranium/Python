import re


def main(input_string):
    pattern = (r'<section>\s*val\s*list\(\s*(-?\d+)\s*,\s*(-?\d+)'
               r'\s*,?\s*(-?\d+)?\s*,?\s*(-?\d+)'
               r'?\s*\)\s*->\s*"(\w+)"\s*</section>')
    matches = re.findall(pattern, input_string)
    result = {}
    for match in matches:
        key = match[-1]
        values = [int(val) for val in match[:-1] if val != '']
        result[key] = values
    return result


input_string_1 = '<section>val list( 6413,4852) -> "enzaar" </section> <section> val list( 8782 , -5084 ) ->"qucequ_925"</section>'
input_string_2 = '<section> val list(-2052 ,7464 ,-6469 ) -> "reveen"</section><section> val list(-9037 , -1104 , -4570 ,-9354 ) ->"geatza" </section>'

result_1 = main(input_string_1)
result_2 = main(input_string_2)

print("Разобранный результат 1:")
print(result_1)
print("\nРазобранный результат 2:")
print(result_2)
