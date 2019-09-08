def linearSearch(someList, target):
    for i in range(len(someList)):
        if (target == someList[i]):
            return i

def main():
    someList = [8, 6, 5, 4, 3, 56, 77, 4, 1]
    target = 77
    print(linearSearch(someList, target))

if __name__ == '__main__':
    main()

