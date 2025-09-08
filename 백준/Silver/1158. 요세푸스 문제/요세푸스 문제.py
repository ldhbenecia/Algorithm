from collections import deque

n, k = map(int, input().split())

people = deque(range(1, n + 1))
killed = []

while people:

    # k번째 사람을 제일 앞으로 뺀다.
    # 빼기 위해서는 그만큼의 앞에 사람을 빼서 뒤로 넣으면 된다.
    for i in range(k - 1):
        people.append(people.popleft())
    killed.append(people.popleft())

print("<" + ", ".join(map(str, killed)) + ">")
