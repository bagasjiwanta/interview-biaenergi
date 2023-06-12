import random
import time


def intersect(bagA: set, bagB: set) -> list:
    '''find intersect(s) in bagA and bagB'''
    result = []
    for o in bagA:
        if o in bagB:
            result.append(o)
    return result


def intersect_v2(bagA: set, bagB: set) -> list:
    '''find intersect(s) in bagA and bagB'''
    return list(set.intersection(bagA, bagB))


def intersect_v3(bagA: set, bagB: set) -> list:
    '''find intersect(s) in bagA and bagB'''
    result = []
    if len(bagA) > len(bagB):
        [bagA, bagB] = [bagB, bagA]

    for o in bagA:
        if o in bagB:
            result.append(o)

    return result


def generate_set_with_length(l: int) -> set:
    '''Generate set s with len(s) close to l'''
    return set(random.randint(0, 1000000000) for _i in range(l))


def measure_time(f) -> tuple:
    '''Measure time execution of a function'''
    start = time.time()
    value = f()
    end = time.time()
    return (end-start, value)


if __name__ == "__main__":
    small_set = generate_set_with_length(100)
    large_set = generate_set_with_length(10000000)
    answer = intersect(large_set, small_set).sort()

    (case1, value) = measure_time(lambda: intersect_v2(large_set, small_set))
    (case2, value) = measure_time(lambda: intersect_v2(small_set, large_set))

    print("Correct:", answer == value.sort())
    print("case 1:", case1, "s, case 2:", case2, "s")
