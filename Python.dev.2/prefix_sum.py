# return a new list, the i-th value in the new list
# is the sum of 0-th value to the i-th value in arr
# example:
# arr: [10, 3, 7, 6, 5, 2]
# prefix sum of arr: [10, 13, 20, 26, 31, 33]

def prefix_sum(arr):
    result = []

    prefix_sum_so_far = 0
    for num in arr:
        prefix_sum_so_far += num
        result.append(prefix_sum_so_far)

    return result


if __name__ == '__main__':
    arr = [10, 3, 7, 6, 5, 2]
    ps = prefix_sum(arr)
    print(arr) # [10, 3, 7, 6, 5, 2]
    print(ps) # [10, 13, 20, 26, 31, 33]