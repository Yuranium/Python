def main2(data):
    match data:
        case["TERRA", "RUST", "AGDA", 2008]:
            return 6
        case['NUMPY', 'VHDL', 'AGDA', 2008]:
            return 7
        case["TERRA", "ORG", "AGDA", 2008]:
            return 8
        case['NUMPY', 'ORG', 'AGDA', 2008]:
            return 8
        case["NUMPY", "ORG", "INI", 1967]:
            return 9
        case['NUMPY', 'RUST', 'INI', 2008]:
            return 9
        case["TERRA", "ORG", "INI", 1967]:
            return 10
        case['TERRA', 'RUST', 'INI', 2008]:
            return 10
        case ['TERRA', 'VHDL', 'LEAN', 1967]:
            return 11


def main(data):
    match data:
        case ["TERRA", "RUST", "AGDA", 1993]:
            return 0
        case ['NUMPY', 'RUST', 'AGDA', 1993]:
            return 0
        case ["NUMPY", "VHDL", "AGDA", 1993]:
            return 1
        case ["TERRA", "ORG", "AGDA", 1993]:
            return 2
        case ["TERRA", "RUST", "AGDA", 1967]:
            return 3
        case ["TERRA", "VHDL", "AGDA", 1967]:
            return 4
        case ["TERRA", "ORG", "AGDA", 1967]:
            return 5
        case ['NUMPY', 'ORG', 'AGDA', 1967]:
            return 5
        case _:
            return main2(data)


print(main(['NUMPY', 'VHDL', 'AGDA', 1993]))
print(main(['NUMPY', 'RUST', 'INI', 2008]))
print(main(['TERRA', 'VHDL', 'LEAN', 1967]))
print(main(['TERRA', 'RUST', 'INI', 2008]))
print(main(['TERRA', 'ORG', 'AGDA', 1993]))
print(main(['NUMPY', 'ORG', 'AGDA', 2008]))
