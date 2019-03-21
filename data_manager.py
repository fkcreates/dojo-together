def get_statistics(filename="request-count.txt"):
    counters = {}
    with open(filename) as file:
        for line in file:
            key, value = line.strip().split(": ")
            counters[key] = int(value)

    return counters


def write_statistics(counters, filename="request-count.txt"):
    with open(filename, "w") as file:
        for key, value in counters.items():
            file.write(f"{key}: {value}\n")


