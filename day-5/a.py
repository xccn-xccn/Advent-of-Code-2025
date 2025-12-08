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
    fresh, available = [x.split() for x in read_file(get_input_file()).split("\n\n")]

    fresh = sorted([tuple(map(int, x.split("-"))) for x in fresh])
    available = sorted(list(map(int, available)))
    i = 0
    count = 0
    
    for a_id in available:
        while i <= len(fresh) - 1:
            f_start, f_end = fresh[i]

            if a_id > f_end:
                i += 1
            else:
                if a_id >= f_start:
                    count += 1
                break

    return count


if __name__ == "__main__":
    start = perf_counter()
    print(main())
    print(f"Time taken: {(perf_counter() - start) *1000} miliseconds")
