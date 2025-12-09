from sys import argv
from time import perf_counter
from collections import Counter


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
    text = read_file(get_input_file()).splitlines()

    for i, square in enumerate(text[0]):
        if square == "S":
            xs = Counter([i])

    for line in text[1:]:
        new_xs = Counter()
        for x, amount in xs.items():
            if line[x] == "^":

                for px in (x - 1, x + 1):
                    if px < 0 or px >= len(line):
                        continue
                    new_xs[px] += amount


            else:
                new_xs[x] += amount

        xs = new_xs

    return sum(xs.values())


if __name__ == "__main__":
    start = perf_counter()
    print(main())
    print(f"Time taken: {(perf_counter() - start) *1000} miliseconds")
