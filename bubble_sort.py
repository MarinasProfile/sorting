# Bubble sort
def bubble_sort(unsorted_list):
    if len(unsorted_list) == 1:
        return unsorted_list

    while True:
        swapped = False
        for i in range(1, len(unsorted_list)):
            if unsorted_list[i] < unsorted_list[i-1]:
                unsorted_list[i], unsorted_list[i-1] = unsorted_list[i-1], unsorted_list[i]
                swapped = True
        if swapped is False:
            return unsorted_list


def test_buble_sort():
    test_lists = [
        [49, 88, 75, 62, 51, 18, 38, 54, 9, 55],
        [84, 24, 86, 2, 6, 71, 3, 22, 97, 83],
        [35, 79, 10, 91, 54, 25, 43, 28, 3, 44],
        [2, 76, 36, 82, 93, 31, 56, 51, 59, 98],
        [26, 1, 81, 82, 74, 37, 54, 54, 24, 6]
    ]

    for l in test_lists:
        assert bubble_sort(l) == sorted(l)
        print("OK")

test_buble_sort()