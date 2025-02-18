"""
This method will parse the input-list.txt file and generaste a python tuple
of each word to be used with the machine learning algorithm.
"""
def parse_inputs(file="input-list.txt"):
    inputs = {}
    with open(file, 'r') as f:
        for word in f.readlines():
            inputs[word.strip()] = 0
    return inputs