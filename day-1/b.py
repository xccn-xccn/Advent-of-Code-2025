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
    count, pos = 0, 50

    last_zero = False
    for line in text:
        pos += int(line[1:]) * (1 if line[0] == 'R' else -1)
        if pos <= 0 or pos >= 100: 
            diff = -pos if pos <= 0 else pos - 100
            count += abs(diff // 100) + (0 if last_zero and pos <= 0 else 1)

        pos = pos % 100
        last_zero = pos == 0
        
    return count


if __name__ == "__main__":
    start = perf_counter()
    print(main())
    print(f'Time taken: {(perf_counter() - start) *1000} miliseconds')