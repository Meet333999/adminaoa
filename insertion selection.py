def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = [11,65,35,87,67,98,90,78,69,8]
insertion_sort(arr)
print("Insertion Sort:")
print("Sorted array:", arr)

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

arr = [11,65,35,87,67,98,90,78,69,8]
selection_sort(arr)
print("Selection Sort:")
print("Sorted array:", arr)

algo
Algorithm INSERTION-SORT() :
function insertionSort(array)
for index from 1 to length(array)
key = array[index]
j = index - 1
while j >= 0 and array[j] > key
array[j + 1] = array[j]
j = j - 1
array[j + 1] = key

Algorithm SELECTION-SORT() :
SelectionSort(arr, n)
declare i, j, minIndex, temp
for i = 0 to n - 1 do
minIndex = i
for j = i + 1 to n - 1 do
if arr[j] < arr[minIndex] then
minIndex = j
end if
end for
temp = arr[i]
arr[i] = arr[minIndex]
arr[minIndex] = temp
end for
