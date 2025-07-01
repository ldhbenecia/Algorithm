n = int(input())

team1_score = 0
team2_score = 0
team1_time = 0
team2_time = 0

prev_time = 0  # 마지막 리드 변경 시점
lead_team = 0  # 현재 리드 팀 (0=무승부, 1=팀1, 2=팀2)


def to_sec(time):
    m, s = map(int, time.split(":"))
    return m * 60 + s


def to_str(sec):
    return f"{sec // 60:02d}:{sec % 60:02d}"


for _ in range(n):
    team, time = input().split()
    current_time = to_sec(time)

    if team == "1":
        team1_score += 1
    else:
        team2_score += 1

    if team1_score > team2_score:
        if lead_team == 2:
            team2_time += current_time - prev_time  # 이전 리드 종료 → 시간 누적
        if lead_team != 1:
            prev_time = current_time  # 리드 바뀐 시점 저장
            lead_team = 1  # 현재 리드 팀 갱신

    elif team2_score > team1_score:
        if lead_team == 1:
            team1_time += current_time - prev_time  # 이전 리드 종료 → 시간 누적
        if lead_team != 2:
            prev_time = current_time  # 리드 바뀐 시점 저장
            lead_team = 2  # 현재 리드 팀 갱신

    else:  # 동점
        if lead_team == 1:
            team1_time += current_time - prev_time
        elif lead_team == 2:
            team2_time += current_time - prev_time
        lead_team = 0

end_time = 48 * 60
if lead_team == 1:
    team1_time += end_time - prev_time
elif lead_team == 2:
    team2_time += end_time - prev_time

print(to_str(team1_time))
print(to_str(team2_time))
