
def binary(target, int_list, start, end):

    mid = (start + end)//2

    if int_list[mid] == target:
        return mid

    elif start >= mid:
        return -1

    elif int_list[mid] > target:
        return binary(target, int_list, start, mid)

    elif int_list[mid] < target:
        return binary(target, int_list, mid, end)

    else:
        return -1

def main():
    int_list = [11, 22, 33, 44, 55, 66, 77, 88, 99]

    print(binary(11, int_list, 0, len(int_list)))
    print(binary(22, int_list, 0, len(int_list)))
    print(binary(33, int_list, 0, len(int_list)))
    print(binary(5, int_list, 0, len(int_list)))
    print(binary(100, int_list, 0, len(int_list)))

if __name__ == "__main__":
    main()


