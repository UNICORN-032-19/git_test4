from calc import Calculator, UnknownOperation, UnknownError

INPUT_FILENAME = "input.txt"
OUTPUT_FILENAME = "output.txt"

def get_data():
    with open(INPUT_FILENAME) as file:
        data = file.readlines()
    data = [x.strip() for x in data]
    return data
