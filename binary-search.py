
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
         if arr[mid] < x:
            low = mid + 1
 
        elif arr[mid] > x:
            high = mid - 1
 
        else:
            return mid
 
    return None
 
 
arr = [ 64, 1, 37, 50, 700 ]
x = 10
 
result = binary_search(arr, x)
 
if result != None:
    print("Element exists at index", str(result))
else:
    print("Element is not in the array")