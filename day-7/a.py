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
    text = read_file(get_input_file()).splitlines()

    for i, square in enumerate(text[0]):
        if square == "S":
            xs = [i]

    count = 0
    for line in text[1:]:
        new_xs = []
        for x in xs:
            if line[x] == "^":

                for px in (x - 1, x + 1):
                    if px < 0 or px >= len(line):
                        continue
                    new_xs.append(px)

                count += 1 if x not in (0, len(line) - 1) else 0

            else:
                new_xs.append(x)

        xs = list(set(new_xs))

    return count


if __name__ == "__main__":
    start = perf_counter()
    print(main())
    print(f"Time taken: {(perf_counter() - start) *1000} miliseconds")
