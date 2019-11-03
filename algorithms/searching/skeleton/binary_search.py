import random
import bisect

def binary_search(int_list, target, start, end):
    # TODO: Fill this in.


    if target < int_list[end//2]:
        return binary_search(int_list, target, start, end//2)

    elif target == int_list[end//2]:
        return end//2

    elif target > int_list[end//2]:
        return binary_search(int_list, target, end//2, end)

    else:
        return -1

#def search(int_list, target, x, y):
#    for i in range(x, y):
#        if int_list[i]== target:
#            return i
#    return -1


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
