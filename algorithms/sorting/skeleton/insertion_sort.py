import random

def insertion_sort(int_list):
    # TODO: Fill this in

#   Insertion-Sort(A)
#   for j = 2 to A.length
#      key = A[j]
#      //insert A[j] into the sorted sequence A[1..j-1]
#   i = j - 1
#   while i > 0 and A[i] > key
#      A[i + 1] = A[i]
#      i = i - 1
#   A[i + 1] = key


    for x in range(1, len(int_list)):

        key = int_list[x]

        y = x - 1

        while y >= 0 and int_list[y] > key:
            int_list[y + 1] = int_list[y]
            y = y - 1

        int_list[y + 1] = key


def check(sorted_list):
    for i in range(len(sorted_list) - 1):
        if sorted_list[i] > sorted_list[i + 1]:
            return False
    return True

def get_random_list(length, min_int, max_int):
    result = []
    for i in range(length):
        rand_int = random.randrange(min_int, max_int)
        result.append(rand_int)
    return result

def main():
    int_list = [13, 43, 45, 6452, 1, 4, 13, 45, 76, 78, 23, 23]
    insertion_sort(int_list)

    num_tests = 100
    min_int = 1
    max_int = 100000
    rand_length = 10000

    print("Running", num_tests, "tests on lists of length", rand_length)
    pass_cnt = 0
    for i in range(num_tests):
        random_list = get_random_list(rand_length, min_int, max_int)
        insertion_sort(random_list)
        if check(random_list):
            print("PASS")
            pass_cnt += 1
        else:
            print("FAIL")
    print("Passed", pass_cnt, "tests")

if __name__ == "__main__":
    main()
