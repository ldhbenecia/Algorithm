n = int(input())
total_time = 48 * 60
team1_time = 0
team2_time = 0
last_time = 0
lead_team = 0
score1 = 0
score2 = 0

def time_to_seconds(time):
    mm, ss = map(int, time.split(":"))
    return mm * 60 + ss

for _ in range(n):
    team, time = input().split()
    current_time = time_to_seconds(time)

    if lead_team == 1:
        team1_time += current_time - last_time
    elif lead_team == 2:
        team2_time += current_time - last_time

    if team == "1":
        score1 += 1
    else:
        score2 += 1

    if score1 > score2:
        lead_team = 1
    elif score2 > score1:
        lead_team = 2
    else:
        lead_team = 0  # 비기는 경우

    last_time = current_time

if lead_team == 1:
    team1_time += total_time - last_time
elif lead_team == 2:
    team2_time += total_time - last_time

print(f"{team1_time // 60:02d}:{team1_time % 60:02d}")
print(f"{team2_time // 60:02d}:{team2_time % 60:02d}")
