def ransom_note(magazine, ransom):
		
		magazine_hash = {} # decrlaring a dictionary
		
		for i in magazine:
			if i in magazine_hash:
				magazine_hash[i] += 1
			else:
				magazine_hash[i] = 1

		for word in ransom:
			if word in magazine_hash and magazine_hash[word] > 0:
				magazine_hash[word] -= 1
			else:
				return False

		return True
	    

	m, n = map(int, input().strip().split(' '))
	magazine = input().strip().split(' ')
	ransom = input().strip().split(' ')
	answer = ransom_note(magazine, ransom)
	if(answer):
	    print("Yes")
	else:
	    print("No")
