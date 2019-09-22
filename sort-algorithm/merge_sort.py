# -*- coding=utf-8 -*-


def merge(sub_arr1: list, sub_arr2: list):
    i = 0
    j = 0
    merge_arr = []
    while i < len(sub_arr1) and j < len(sub_arr2):
        if sub_arr1[i] < sub_arr2[j]:
            merge_arr.append(sub_arr1[i])
            i = i + 1
        else:
            merge_arr.append(sub_arr2[j])
            j = j + 1
    return merge_arr + sub_arr1[i: len(sub_arr1)] + sub_arr2[j: len(sub_arr2)]


def merge_sort_method(arr: list):
    arr_len = len(arr)
    if arr_len <= 1:
        return arr

    sub_arr1 = arr[0: arr_len//2]
    sub_arr2 = arr[arr_len//2: arr_len]
    sub_arr1 = merge_sort_method(sub_arr1)
    sub_arr2 = merge_sort_method(sub_arr2)
    return merge(sub_arr1, sub_arr2)


if __name__ == "__main__":
    arr = [1, 4, 10, 6, 7, 5, 4, 3, 2, 11, 15, 19, 13]
    print(merge_sort_method(arr))
