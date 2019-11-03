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

if __name__ == "__main__":
    main()
