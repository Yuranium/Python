result = []


class MealyMachine:
    def __init__(self):
        self.state = 'A'

    def jog(self):
        match self.state:
            case 'A':
                self.state = 'B'
                result.append(0)
                return 0
            case 'B':
                self.state = 'H'
                result.append(3)
                return 3
            case 'E':
                self.state = 'B'
                result.append(8)
                return 8
            case 'F':
                self.state = 'G'
                result.append(9)
                return 9
            case 'G':
                self.state = 'B'
                result.append(11)
                return 11
            case _:
                raise MealyError('jog')

    def melt(self):
        match self.state:
            case 'B':
                self.state = 'B'
                result.append(4)
                return 4
            case 'G':
                self.state = 'H'
                result.append(10)
                return 10
            case _:
                raise MealyError('melt')

    def zoom(self):
        match self.state:
            case 'A':
                self.state = 'G'
                result.append(1)
                return 1
            case 'B':
                self.state = 'C'
                result.append(2)
                return 2
            case 'C':
                self.state = 'D'
                result.append(5)
                return 5
            case 'D':
                self.state = 'E'
                result.append(6)
                return 6
            case 'E':
                self.state = 'F'
                result.append(7)
                return 7
            case _:
                raise MealyError('zoom')


class MealyError(Exception):
    def __init__(self, method_name):
        self.method_name = method_name
        global result


def main():
    return MealyMachine()


def test():
    global result
    o = main()
    o.zoom()  # 1
    try:
        o.zoom()  # MealyError
    except MealyError:
        pass
    o.jog()  # 11
    o.melt()  # 4
    o.melt()  # 4
    o.zoom()  # 2
    try:
        o.jog()  # MealyError
    except MealyError:
        pass
    o.zoom()  # 5
    o.zoom()  # 6
    try:
        o.melt()  # MealyError
    except MealyError:
        pass
    o.jog()  # 8
    o.zoom()  # 2
    o.zoom()  # 5
    o.zoom()  # 6
    try:
        o.melt()  # MealyError
    except MealyError:
        pass
    o.zoom()  # 7
    o.jog()  # 9
    o.melt()  # 10

    o = main()
    o.jog()  # 0
    o.zoom()  # 2
    o.zoom()  # 5
    o.zoom()  # 6
    o.zoom()  # 7
    o.jog()  # 9
    o.jog()  # 11
    o.melt()  # 4
    o.melt()  # 4
    o.zoom()  # 2
    o.zoom()  # 5
    o.zoom()  # 6
    o.jog()  # 8
    o.jog()  # 3

    result = []
    try:
        o = main()
        o.zoom()  # 1
        o.jog()  # 11
        o.melt()  # 4
        o.melt()  # 4
        o.zoom()  # 2
        o.zoom()  # 5
        o.zoom()  # 6
        o.melt()  # MealyError
    except MealyError:
        pass

    return result
