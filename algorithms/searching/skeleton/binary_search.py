import random
import bisect

def binary_search(int_list, target, start, end):
    # TODO: Fill this in.

    mid = (start + end)//2

    if target == int_list[mid]:
        return mid

    elif start >= mid:
        return -1

    elif target < int_list[mid]:
        return binary_search(int_list, target, start, mid)

    elif target > int_list[mid]:
        return binary_search(int_list, target, mid, end)

    else:
        return -1

def get_random_list(length, min_int, max_int):
    result = [];
    for i in range(length):
        result.append(random.randrange(min_int, max_int))
    result.sort()
    return result

def get_random_int(min_int, max_int):
    return random.randrange(min_int, max_int)

def check(int_list, target, result):
    if result == -1:
        return not (target in int_list)
    elif result < 0 or result >= len(int_list):
        return False
    return int_list[result] == target

def main():
    # Test01: target is in the list.
    int_list = [1, 2, 6, 12, 67, 199, 233, 651, 1422, 32010]
    print(binary_search(int_list, 233, 0, len(int_list)))

    # Test02: target is not in the list.
    print(binary_search(int_list, 3, 0, len(int_list)))

    # Test03: target is larger than the maximum value in list.
    print(binary_search(int_list, 40000, 0, len(int_list)))

    # Test04: target is smaller than the minimum value in list.
    print(binary_search(int_list, -1, 0, len(int_list)))

    #Test05:
    print(binary_search(int_list, 32010, 0, len(int_list)))

    #Test06:
    print(binary_search(int_list, 1, 0, len(int_list)))

    #Test07:
    print(binary_search(int_list, 6, 0, len(int_list)))

    num_tests = 100
    rand_length = 10000
    min_int = 1
    max_int = 100000
    print("Running", num_tests, "tests on random lists of length", rand_length)
    pass_cnt = 0
    # Test05: Test on random lists.
    for i in range(100):
        random_list = get_random_list(rand_length, min_int, max_int)
        target = get_random_int(min_int, max_int)
        result = binary_search(random_list, target, 0, rand_length)
        if check(random_list, target, result):
            print("PASS")
            pass_cnt += 1
        else:
            print("FAIL")

    print("Passed", pass_cnt, "tests.")

if __name__ == "__main__":
    main()
