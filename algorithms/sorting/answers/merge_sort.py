def merge(list, p, q, r):
    left = []
    for i in range(p, q + 1):
        left.append(list[i])

    right = []
    for j in range(q + 1, r + 1):
        right.append(list[j])

    i = 0
    j = 0
    for k in range(p, r + 1):
        if i < len(left) and j < len(right) and left[i] <= right[j]:
            list[k] = left[i]
            i = i + 1
        elif i < len(left) and j < len(right) and left[i] > right[j]:
            list[k] = right[j]
            j = j + 1
        elif i < len(left) and j >= len(right):
            list[k] = left[i]
            i = i + 1
        elif i >= len(left) and j < len(right):
            list[k] = right[j]
            j = j + 1

def merge_sort(list, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(list, p, q)
        merge_sort(list, q + 1, r)
        merge(list, p, q, r)

def main():
    list = [9, 7,4,2,4,6,7,1,34,67,7,7,4,2,1,56,7,8]
    merge_sort(list, 0, len(list) - 1)
    print(list)

if __name__ == '__main__':
    main()
