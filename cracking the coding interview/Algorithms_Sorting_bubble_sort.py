def bubble_sort(arr):
    num_swaps = 0
    
    if len(arr) < 2:
        return num_swaps
    
    for i in range(len(arr)-1, 0 , -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                num_swaps += 1
                
    return num_swaps
        

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

swaps = bubble_sort(a)

print("Array is sorted in {0} swaps.".format(swaps))
print("First Element: {0}".format(a[0]))
print("Last Element: {0}".format(a[-1]))
