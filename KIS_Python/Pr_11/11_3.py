result = []


class MealyMachine:
    def __init__(self):
        self.state = 'A'
        self.transitions = {
            'jog': {
                'A': ('B', 0),
                'B': ('H', 3),
                'E': ('B', 8),
                'F': ('G', 9),
                'G': ('B', 11)
            },
            'melt': {
                'B': ('B', 4),
                'G': ('H', 10)
            },
            'zoom': {
                'A': ('G', 1),
                'B': ('C', 2),
                'C': ('D', 5),
                'D': ('E', 6),
                'E': ('F', 7)
            }
        }
        global result

    def jog(self):
        return self.transition('jog')

    def melt(self):
        return self.transition('melt')

    def zoom(self):
        return self.transition('zoom')

    def transition(self, action):
        if self.state in self.transitions[action]:
            self.state, res = self.transitions[action][self.state]
            result.append(res)
            return res
        else:
            raise MealyError(action)


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
