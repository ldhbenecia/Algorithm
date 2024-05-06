def solution(s):
    dict = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for i in dict:
        if i in s:
            idx = str(dict.index(i))
            s = s.replace(i, idx)

    return int(s)