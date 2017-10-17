def is_matched(expression):
    lefty = "({["  # opening delimiters
    righty = ")}]" # respective closing delims
    S = []
    
    for c in expression:
        if c in lefty:
            S.append(c) # push left delimiter on stack
        elif c in righty:
            if not S:
                return False # nothing to match with
            if righty.index(c) != lefty.index(S.pop( )):
                return False # mismatched
    if not S:
        return True
    else:
        return False

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")
