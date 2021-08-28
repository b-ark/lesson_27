# A bubble sort can be modified to “bubble” in both directions. The first pass moves “up” the list
# and the second pass moves “down.” This alternating pattern continues until no more passes are necessary.
# Implement this variation and describe under what circumstances it might be appropriate


def cocktail_sort(array):
    n = len(array)
    swapped = True
    start = 0
    end = n - 1
    while swapped:
        swapped = False

        for i in range(start, end):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True

        if not swapped:
            break

        swapped = False
        end = end - 1

        for i in range(end - 1, start - 1, -1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True

        start = start + 1


test_list = [10, 2, 5, 6, 1, 3, 11, 7, 8, 4, 9]
cocktail_sort(test_list)
print(test_list)
