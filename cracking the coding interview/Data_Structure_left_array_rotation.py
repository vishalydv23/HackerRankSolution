# A Juggling Algorith

# Instead of moving one by one, divide the array in different sets
# where number of sets is equal to GCD of n and d and move the elements within sets.
# If GCD is 1 as is for the above example array (n = 7 and d =2), then elements will be 
# moved within one set only, we just start with temp = arr[0] and keep moving arr[I+d] to arr[I] 
# and finally store temp at the right place.

def gcdfunction(a, b):
    if(b == 0):
        return a
    else:
        return gcdfunction(b, a % b)
    

def array_left_rotation(a, n, d):
    gcd = gcdfunction(d, n)
    for i in range(gcd):
        temp = a[i]
        j = i
        while True:
            k = j + d
            if( k >= n):
                k = k - n
            if k == i:
                break
            a[j] = a[k]
            j = k
        a[j] = temp
    return a 
    

n, d = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, d);
print(*answer, sep=' ')
