n, m = map(int, input().split())
know = list(map(int, input().split()))

party_person = []
for _ in range(m):
    party_person.append(list(map(int, input().split())))

know_cnt = know[0]
know_person = set(know[1:])

# 진실을 아는 사람이 없을 경우
if know_cnt == 0:
    print(m)
else:
    updated = True
    while updated:
        updated = False
        for i in party_person:
            person_cnt = i[0]
            person = set(i[1:])
            if know_person & person: # 교집합이 존재하면 진실을 아는 사람이 있는 것
                if not person.issubset(know_person): # 진실 아는 사람 추가 갱신
                    know_person.update(person)
                    updated = True
    
    result = 0
    for i in party_person:
        person_cnt = i[0]
        person = set(i[1:])
        if not know_person & person:
            result += 1

    print(result)