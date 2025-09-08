t = int(input())

command = ["<", ">", "-"]
for _ in range(t):
    key = input()

    # Cursor를 기점으로 왼쪽 배열과 오른쪽 배열을 분리
    left = []
    right = []
    for i in key:
        if i not in command:
            left.append(i)  # 커서는 값을 입력하고 다음 값으로
        else:
            if i == "<":
                if left:
                    right.append(left.pop())
            elif i == ">":
                if right:
                    left.append(right.pop())
            else:
                if left:
                    left.pop()

    left.extend(reversed(right))
    print("".join(left))
