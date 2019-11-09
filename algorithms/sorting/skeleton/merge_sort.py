import random

def merge(some_list, p, q, r):
    # TODO: fill this.
    left = []
    right = []

    for i in range(p, q + 1):
        left.append(some_list[i])

    for i in range(q + 1, r + 1):
        right.append(some_list[i])

    i = 0
    j = 0
    for k in range(p, r + 1):
        if i >= len(left):
            some_list[k] = right[j]
            j = j + 1
        elif j >= len(right):
            some_list[k] = left[i]
            i = i + 1
        elif left[i] <= right[j]:
            some_list[k] = left[i]
            i = i + 1
        else:
            some_list[k] = right[j]
            j = j + 1

def merge_sort(some_list, p, r):
    # TODO: fill this.
    if p < r:
        q = (p + r)//2
        merge_sort(some_list, p, q)
        merge_sort(some_list, q + 1, r)
        merge(some_list, p, q, r)

def main():
    rand_list = []
    for i in range(100):
        rand_list.append(random.randrange(1, 100))
    print(rand_list)
    some_list = [8, 7, 6, 5, 4, 3, 2, 1]
    #some_list = [12, 55, 2, 9, 11, 34]
    merge_sort(rand_list, 0, len(rand_list) - 1)
    print(rand_list)

if __name__ == "__main__":
    main()
