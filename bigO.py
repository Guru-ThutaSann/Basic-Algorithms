#simple linear search algorithm:
def linear_search(arr, target):
    for element in arr:
        if element == target:
            return True
    return False

#bubble sort algorithm:
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]



# Example usage - linear search
my_list = [1, 2, 3, 4, 5]
target_value = 3

result = linear_search(my_list, target_value)

if result:
    print(f"{target_value} found in the list.")
else:
    print(f"{target_value} not found in the list.")
    
'''
# Example usage - bubble sort
my_list = [64, 34, 25, 12, 22, 11, 90]

bubble_sort(my_list)

print("Sorted array:", my_list)
'''