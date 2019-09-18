# -*- coding=utf-8 -*-


def sub_arr_sort(arr: list):
    if not arr or len(arr) == 1:
        return arr

    pre_arr = []
    late_arr = []
    for i in range(len(arr)-1):
        if arr[i+1] < arr[0]:
            pre_arr.append(arr[i+1])
        else:
            late_arr.append(arr[i+1])
    return sub_arr_sort(pre_arr) + [arr[0]] + sub_arr_sort(late_arr)


def quick_sort_method(arr: list):
    return sub_arr_sort(arr)


def partition(arr, left_idx, right_idx, pivot_idx):
    compare_val = arr[pivot_idx]
    i = left_idx
    j = right_idx
    while i < j:
        if i == pivot_idx:
            temp = arr[i]
            pivot_idx = pivot_idx + 1
            arr[i] = arr[pivot_idx]
            arr[pivot_idx] = temp
        if arr[i] > compare_val:
            if j > pivot_idx:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                j = j - 1
            else:
                temp = arr[pivot_idx]
                arr[pivot_idx] = arr[pivot_idx - 1]
                arr[pivot_idx - 1] = temp
                pivot_idx = pivot_idx - 1
                j = pivot_idx
        else:
            i = i + 1
    return pivot_idx


def quick_sort_method_2(arr: list, left_idx, right_idx):
    if left_idx < right_idx:
        pivot_idx = left_idx
        pivot_new_idx = partition(arr, left_idx, right_idx, pivot_idx)
        quick_sort_method_2(arr, left_idx, pivot_new_idx - 1)
        quick_sort_method_2(arr, pivot_new_idx + 1, right_idx)


if __name__ == "__main__":
    arr = [1, 4, 10, 6, 7, 5, 4, 3, 2, 11, 15, 19, 13]
    print(quick_sort_method(arr))

    quick_sort_method_2(arr, 0, 12)
    print(arr)
