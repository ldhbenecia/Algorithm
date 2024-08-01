import math

def converter_time(HHMM):
    hour, minute = HHMM.split(":")
    result = int(hour) * 60 + int(minute)
    return result
    

def solution(fees, records):
    answer = []

    basic_time = fees[0] # 기본 시간
    basic_price = fees[1] # 기본 요금
    unit_time = fees[2] # 단위 시간
    unit_price = fees[3] # 단위 요금
    last_time = converter_time("23:59")
    
    dic = {}
    price_dic = {}
    for record in records:
        hhmm, num, inout = record.split(" ")
        minute = converter_time(hhmm)
        
        # 입차
        if num not in dic:
            dic[num] = minute
        # 출차
        else:
            in_time = dic[num]
            difference = minute - in_time
            if num not in price_dic:
                price_dic[num] = difference
            else:
                price_dic[num] += difference
            del dic[num]
        
    # 입차 이후 출차가 없는 경우 (dic에 값이 남아있음)
    if dic:
        for num in list(dic.keys()):
            time = dic[num]
            difference = last_time - time
            if num not in price_dic:
                price_dic[num] = difference
            else:
                price_dic[num] += difference
            del dic[num] 
    
    # 차량 번호가 작은 자동차부터 청구할 주차 요금을 차례대로 정수 배열에 담아서 return
    for i in sorted(price_dic.items()):
        num, difference = i[0], i[1]
        if difference <= basic_time:
            answer.append(basic_price)
        else:
            express = basic_price + math.ceil((difference - basic_time) / unit_time) * unit_price
            answer.append(express)
            
    return answer

