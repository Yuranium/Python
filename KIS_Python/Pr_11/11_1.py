result = []


class MealyMachine:
    def __init__(self):
        self.state = 'A'

    def jog(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'H'
            return 3
        elif self.state == 'E':
            self.state = 'B'
            return 8
        elif self.state == 'F':
            self.state = 'G'
            return 9
        elif self.state == 'G':
            self.state = 'B'
            return 11
        else:
            raise MealyError("jog")

    def melt(self):
        if self.state == 'B':
            self.state = 'B'
            return 4
        elif self.state == 'G':
            self.state = 'H'
            return 10
        else:
            raise MealyError("melt")

    def zoom(self):
        if self.state == 'A':
            self.state = 'G'
            return 1
        elif self.state == 'B':
            self.state = 'C'
            return 2
        elif self.state == 'C':
            self.state = 'D'
            return 5
        elif self.state == 'D':
            self.state = 'E'
            return 6
        elif self.state == 'E':
            self.state = 'F'
            return 7
        else:
            raise MealyError("zoom")


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
