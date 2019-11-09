
def binary(x, list, s, e):

    m = (s + e)//2

    if list[m] == x:
        return m

    elif s >= m:
        return -1

    elif list[m] < x:
        return binary(x, list, m, e)

    elif list[m] > x:
        return binary(x, list, s, m)

    else:
        return -1



def main():
    list = [12, 23, 34, 45, 56, 67, 78, 89, 90]

    print(binary(12, list, 0, len(list)))

    print(binary(90, list, 0, len(list)))

    print(binary(5, list, 0, len(list)))

    print(binary(99, list, 0, len(list)))

    print(binary(34, list, 0, len(list)))

    print(binary(89, list, 0, len(list)))

if __name__ == "__main__":
    main()


