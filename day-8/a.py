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


def calc_distance(c1, c2):
    count = 0
    for i in range(len(c1)):
        count += (c1[i] - c2[i]) ** 2

    return count


def main():
    text = [
        tuple(map(int, x.split(","))) for x in read_file(get_input_file()).splitlines()
    ]

    circuits = []
    seen = set()

    for box in text:
        close_d, close_box = float("inf"), None

        for p_box in text:
            if p_box == box:
                continue

            p_dist = calc_distance(box, p_box)

            if p_dist < close_d:
                close_d, close_box = p_dist, p_box

        if close_box not in seen and box not in seen:
            circuits.append({close_box, box})
            seen.update({close_box, box})
        elif close_box not in seen:
            seen.add(close_box)
            for i, circ in enumerate(circuits):
                if box in circ:
                    circuits[i].add(close_box)
                    break

        elif box not in seen:
            seen.add(box)

            for i, circ in enumerate(circuits):
                if close_box in circ:
                    circuits[i].add(box)
                    break
        else:
            inds = []
            circs = []
            for i, circ in enumerate(circuits):
                if box in circ or close_box in circ:
                    inds.append(i)
                    circs.append(circ)

            if len(inds) == 2:
                circuits[inds[0]].update(circuits[inds[1]])

                # circuits[inds[1]] = {}
                del circuits[inds[1]]
            else:
                print("same", inds, circs)

        # print(circuits)

    count = 1
    print(sorted(circuits, key=len, reverse=True))
    for c in sorted(circuits, key=len, reverse=True)[:3]:
        count *= len(c)

    return count


if __name__ == "__main__":
    start = perf_counter()
    print(main())
    print(f"Time taken: {(perf_counter() - start) *1000} miliseconds")
