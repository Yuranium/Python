def _3(array):
    if array[1] == "ORG":
        return 2
    elif array[1] == "VHDL":
        return 1
    else:
        return 0


def _4(array):
    if array[1] == "ORG":
        return 5
    elif array[1] == "VHDL":
        return 4
    else:
        return 3


def agda(array):
    if array[3] == 2008:
        if array[1] == "ORG":
            return 8
        elif array[1] == "VHDL":
            return 7
        else:
            return 6
    elif array[3] == 1967:
        return _4(array)
    else:
        return _3(array)


def ini(array):
    if array[0] == "NUMPY":
        return 9
    else:
        return 10


def main(array):
    if array[2] == "LEAN":
        return 11
    elif array[2] == "INI":
        return ini(array)
    else:
        return agda(array)


print(main(['NUMPY', 'VHDL', 'AGDA', 1993]))
print(main(['NUMPY', 'RUST', 'INI', 2008]))
print(main(['TERRA', 'VHDL', 'LEAN', 1967]))
print(main(['TERRA', 'RUST', 'INI', 2008]))
print(main(['TERRA', 'ORG', 'AGDA', 1993]))
