def solution(answers):
    answer = []
    a1 = [1, 2, 3, 4, 5]
    a2 = [2, 1, 2, 3, 2, 4, 2, 5]
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    correct = {"1": 0, "2": 0, "3": 0}

    for i in range(len(answers)):
        if answers[i] == a1[i % 5]:
            correct["1"] += 1
        if answers[i] == a2[i % 8]:
            correct["2"] += 1
        if answers[i] == a3[i % 10]:
            correct["3"] += 1
    
    max_value = max(correct.values())
    max_list = []
    for key, value in correct.items():
        if max_value == value:
            max_list.append(key)
    
    if len(max_list) == 1:
        return list(map(int, max_list))
    else:
        max_list.sort()
        return list(map(int, max_list))
