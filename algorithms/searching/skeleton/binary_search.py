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

if __name__ == "__main__":
    main()
