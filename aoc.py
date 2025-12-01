""" Common code for AOC 2025 """

def read_file(name):
    with open(name, 'r') as fhan:
        return ''.join(fhan.readlines())
