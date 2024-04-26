def solution(bandage, health, attacks):
    continuity = 0 # 연속 성공
    last_attack_time = max(attacks)[0] # 마지막 공격이 이루어지는 시간초
    attack_dict = {}
    max_health = health
    
    for i in attacks:
        attack_dict[i[0]] = i[1]
    
    for i in range(1, last_attack_time + 1):
        if i in attack_dict:
            health -= attack_dict[i]
            continuity = 0
            if health <= 0:
                return -1
        else:
            continuity += 1
            if continuity < bandage[0]:
                health += bandage[1]
                if health > max_health:
                    health = max_health
            else:
                health += bandage[1] + bandage[2]
                continuity = 0
                if health > max_health:
                    health = max_health

    return health