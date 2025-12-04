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


def get_biggest(line):
    return max(enumerate(line), key=lambda x: (x[1], -x[0]))


def main():
    text = read_file(get_input_file()).splitlines()
    count = 0
    for line in text:
        i, n = get_biggest(line)

        if i == len(line) - 1:
            n = get_biggest(line[:-1])[1] + n
        else:
            n = n + get_biggest(line[i + 1 :])[1]

        count += int(n)

    return count


if __name__ == "__main__":
    start = perf_counter()
    print(main())
    print(f"Time taken: {(perf_counter() - start) *1000} miliseconds")
