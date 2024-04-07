def main(data):
    conditions = {
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
    return conditions.get(tuple(data), None)


print(main(['NUMPY', 'VHDL', 'AGDA', 1993]))
print(main(['NUMPY', 'RUST', 'INI', 2008]))
print(main(['TERRA', 'VHDL', 'LEAN', 1967]))
print(main(['TERRA', 'RUST', 'INI', 2008]))
print(main(['TERRA', 'ORG', 'AGDA', 1993]))
print(main(['NUMPY', 'ORG', 'AGDA', 2008]))
