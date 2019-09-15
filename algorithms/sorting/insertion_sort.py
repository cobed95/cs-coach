def insertion_sort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j = j - 1
        list[j + 1] = key

def main():
    list = [6, 3, 2, 6, 6, 8, 2, 9, 1, 2, 5, 2]
    insertion_sort(list)
    print(list)

if __name__ == '__main__':
    main()
