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
    text = [
        r.split("-") for r in "".join(read_file(get_input_file()).split()).split(",")
    ]

    count = 0
    for start, end in text:
        for n in range(int(start), int(end) + 1):
            str_n = str(n)
            mid = len(str_n) // 2

            if str_n == str_n[:mid] + str_n[:mid]:
                count += n

    return count


if __name__ == "__main__":
    start = perf_counter()
    print(main())
    print(f"Time taken: {(perf_counter() - start) *1000} miliseconds")
