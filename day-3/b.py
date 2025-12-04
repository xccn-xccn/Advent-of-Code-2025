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
        start = end = ""
        length = 0
        while length < 12:
            n_i, n = get_biggest(line)

            if n_i >= len(line) - (12 - length):
                end = line[n_i:] + end
                line = line[:n_i]
            else:
                line = line[n_i + 1 :]
                start += n

            length = len(start) + len(end)

        count += int(start + end)

    return count


if __name__ == "__main__":
    start = perf_counter()
    print(main())
    print(f"Time taken: {(perf_counter() - start) *1000} miliseconds")
