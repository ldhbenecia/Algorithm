def is_palindrome(s):
    if s[::] == s[::-1]:
        return True
    
    return False

s = input()

if is_palindrome(s):
    print(len(s))
else:
    for i in range(len(s)):
        if s[i:] == s[i:][::-1]:
            print(len(s) + i)
            break