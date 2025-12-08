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
    numbers = text[:-1]

    operators = text[-1].split()
    count = 0

    op_i = 0

    calculation = 0 if operators[0] == "+" else 1
    f = op_dict[operators[0]]
    for i in range(len(numbers[0])):

        str_num = ""
        for line in numbers:
            num = line[i]

            if num != " ":
                str_num += num

        if str_num:
            num = int(str_num)
            calculation = f(calculation, num)
        else:
            count += calculation
            op_i += 1

            f = op_dict[operators[op_i]]
            calculation = 0 if operators[op_i] == "+" else 1

    return count + calculation


if __name__ == "__main__":
    start = perf_counter()
    print(main())
    print(f"Time taken: {(perf_counter() - start) *1000} miliseconds")
