class DecisionTree:
    def __init__(self, threshold=None, value=None, children=None):
        self.threshold = threshold
        self.value = value
        self.children = children if children is not None else {}

    def fit(self, data_points):
        for data_point, result in data_points.items():
            node = self
            for feature in data_point:
                if feature not in node.children:
                    node.children[feature] = DecisionTree()
                node = node.children[feature]
            node.value = result

    def predict(self, data_point):
        node = self
        for feature in data_point:
            if feature not in node.children:
                return None
            node = node.children[feature]
        return node.value


def main(data):  # Способ 5
    tree = DecisionTree()
    data_points = {
        ("TERRA", "RUST", "AGDA", 1993): 0,
        ("TERRA", "VHDL", "AGDA", 1993): 1,
        ("TERRA", "ORG", "AGDA", 1993): 2,
        ("TERRA", "RUST", "AGDA", 1967): 3,
        ("TERRA", "VHDL", "AGDA", 1967): 4,
        ("TERRA", "ORG", "AGDA", 1967): 5,
        ("TERRA", "RUST", "AGDA", 2008): 6,
        ("TERRA", "VHDL", "AGDA", 2008): 7,
        ("TERRA", "ORG", "AGDA", 2008): 8,
        ("NUMPY", "ORG", "INI", 1967): 9,
        ("TERRA", "ORG", "INI", 1967): 10,
        ("TERRA", "RUST", "LEAN", 2008): 11,
        ('NUMPY', 'VHDL', 'AGDA', 1993): 1,
        ('NUMPY', 'RUST', 'INI', 2008): 9,
        ('TERRA', 'VHDL', 'LEAN', 1967): 11,
        ('TERRA', 'RUST', 'INI', 2008): 10,
        ('NUMPY', 'ORG', 'AGDA', 2008): 8,
        ('NUMPY', 'ORG', 'AGDA', 1967): 5,
        ('NUMPY', 'RUST', 'AGDA', 1993): 0,
        ('NUMPY', 'VHDL', 'AGDA', 2008): 7
    }
    tree.fit(data_points)
    return tree.predict(data)


print(main(['NUMPY', 'VHDL', 'AGDA', 1993]))
print(main(['NUMPY', 'RUST', 'INI', 2008]))
print(main(['TERRA', 'VHDL', 'LEAN', 1967]))
print(main(['TERRA', 'RUST', 'INI', 2008]))
print(main(['TERRA', 'ORG', 'AGDA', 1993]))
print(main(['NUMPY', 'ORG', 'AGDA', 2008]))
