from sys import argv
from time import perf_counter
from itertools import product


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

    valid_count = 0
    for y, row in enumerate(text):
        for x, square in enumerate(row):
            if square == ".":
                continue

            roll_count = 0
            for dx, dy in product((-1, 0, 1), repeat=2):
                px, py = x + dx, y + dy

                if (
                    px < 0
                    or py < 0
                    or px >= len(row)
                    or py >= len(text)
                    or dx == dy == 0
                ):
                    continue

                if text[py][px] == "@":
                    roll_count += 1

            valid_count += 1 if roll_count < 4 else 0

    return valid_count


if __name__ == "__main__":
    start = perf_counter()
    print(main())
    print(f"Time taken: {(perf_counter() - start) *1000} miliseconds")
