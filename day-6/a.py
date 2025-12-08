from sys import argv
from time import perf_counter


def read_file(filename):
    with open(filename) as file:
        text = file.read()
    return text


def get_input_file():
    if len(argv) == 1:
        return "sample.txt"
    elif len(argv) == 2:
        return argv[1] if argv[1] != "i" else "input.txt"


def main():
    op_dict = {"*": lambda x, y: x * y, "+": lambda x, y: x + y}
    text = read_file(get_input_file()).splitlines()
    numbers = [list(map(int, x.split())) for x in text[:-1]]

    operators = text[-1].split()
    count = 0
    for i in range(len(numbers[0])):

        f = op_dict[operators[i]]
        calculation = numbers[0][i]
        for line in numbers[1:]:
            calculation = f(calculation, line[i])

        count += calculation

    return count



if __name__ == "__main__":
    start = perf_counter()
    print(main())
    print(f'Time taken: {(perf_counter() - start) *1000} miliseconds')