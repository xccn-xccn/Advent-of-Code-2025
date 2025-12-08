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
    fresh = read_file(get_input_file()).split("\n\n")[0].split()

    fresh = sorted([tuple(map(int, x.split("-"))) for x in fresh])
    
    upper = -1
    count = 0

    for id in fresh:
        l_id, u_id = id
        if upper < l_id:
            count += u_id - l_id + 1
        elif upper < u_id:
            count += u_id - upper
        upper = max(upper, u_id)

    return count


if __name__ == "__main__":
    start = perf_counter()
    print(main())
    print(f"Time taken: {(perf_counter() - start) *1000} miliseconds")
