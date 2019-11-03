def insert(int_list, key):
    if len(int_list) == 0:
        return [key]
    else:
        if int_list[0] <= key:
            return [key] + int_list
        else:
            return [int_list[0]] + insert(int_list[1:], key)

def iterate(loop_invariant, todo):
    if len(todo) == 0:
        return loop_invariant
    else:
        inserted = insert(loop_invariant, todo[0])
        return iterate(inserted, todo[1:])

def reverse(int_list, container):
    if len(int_list) == 0:
        return container
    else:
        return reverse(int_list[1:], [int_list[0]] + container)

def insertion_sort(int_list):
    if len(int_list) == 0:
        return []
    else:
        return reverse(iterate([int_list[0]], int_list[1:]), [])

def main():
    int_list = [1332, 3,2, 334, 6, 61, 2,4, 245, 567, 220, 2, 2324, 45, 23, 21, 1, 1,3]
    print(int_list)
    print(insertion_sort(int_list))

if __name__ == "__main__":
    main()
