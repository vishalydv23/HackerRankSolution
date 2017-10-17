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
