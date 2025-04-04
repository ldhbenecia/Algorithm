s = input()

for i in s:
    asc = ord(i) + 13
    if "a" <= i <= "z":
        if asc > ord("z"):
            asc -= 26
        print(chr(asc), end="")
    elif "A" <= i <= "Z":
        if asc > ord("Z"):
            asc -= 26
        print(chr(asc), end="")
    else:
        print(i, end="")
