def binarySearchIter(someList, target, start, end):
    if start == end:
        if (someList[start] == target):
            return start
        else:
            return -1

    else:
        mid = (start + end) // 2
        if someList[mid] == target:
            return mid
        elif someList[mid] > target:
            return binarySearchIter(someList, target, start, mid)
        else:
            return binarySearchIter(someList, target, mid, end)

def binarySearch(someList, target):
    return binarySearchIter(someList, target, 0, len(someList))

def main():
    someList = [0, 1, 2, 3, 4, 5]
    for i in range(len(someList)):
        print(binarySearch(someList, i))

if __name__ == '__main__':
    main()
