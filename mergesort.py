import time
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

arr = [11,65,35,87,67,98,90,78,69,8]

start_time = time.time()
sorted_arr = merge_sort(arr)
end_time = time.time()

print("Merge Sort:")
print("Sorted array:", sorted_arr)
print("Time taken:", end_time - start_time, "seconds")


algo
function mergeSort(array)
if length of array <= 1
return array
middle = length of array / 2
leftArray = mergeSort(first half of array)
rightArray = mergeSort(second half of array)
return merge(leftArray, rightArray)
