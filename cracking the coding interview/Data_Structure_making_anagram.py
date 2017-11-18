# create an array of size 26 denoting each alphabet and initialize each value as 0.
# read first input array and add 1 for each caracter on place
# read second array and remove 1 for each character
# finally count the total count

a = input()
b = input()
cnt = [0] * 26
offset = ord('a')
for char in a:
	cnt[ord(char) - offset] += 1
for char in b:
	cnt[ord(char) - offset] -= 1
total = 0
for value in cnt:
	total += abs(value)
print(total)
