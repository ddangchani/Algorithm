from datetime import datetime
import math

def solution(fees, records):
    t_def, p_def, t_unit, p_unit = fees
    time_car = {} # 입출차 기록 저장
    dur_car = {} # 총 시간 저장
    res_car = {} # 총 요금 저장
    for rec in records:
        t_rec, car, key = rec.split()
        if car in time_car:
            dur = datetime.strptime(t_rec,'%H:%M') -datetime.strptime(time_car[car],'%H:%M')
            dur = int(dur.seconds/60)
            if car in dur_car:
                dur_car[car] += dur
            else:
                dur_car[car] = dur
            
            del time_car[car]

        else:
            time_car[car] = t_rec
    
    if time_car:
        for car in time_car.keys():
            dur = datetime.strptime('23:59','%H:%M') -datetime.strptime(time_car[car],'%H:%M')
            dur = int(dur.seconds/60)
            if car in dur_car:
                dur_car[car] += dur
            else:
                dur_car[car] = dur
    
    for car in dur_car.keys():
        if dur_car[car] <= t_def:
            res_car[car] = p_def
        else:
            res_car[car] = p_def + math.ceil((dur_car[car]-t_def)/t_unit)*p_unit
    
    answer = [res_car[key] for key in sorted(res_car.keys())]

    return answer

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

print(solution(fees,records))

