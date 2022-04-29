def solution(record):
    commands = []
    uids = []
    dict_id = {}
    for rec in record:
        recs = rec.split(' ')
        command = recs[0]
        uid = recs[1]
        # command 처리 - 들어오면 0 나가면 1
        if command == "Enter": 
            commands.append(0)
            uids.append(uid)
            dict_id[uid] = recs[2]
        elif command == "Leave": 
            commands.append(1)
            uids.append(uid)
        elif command == "Change":
            dict_id[uid] = recs[2]
    # 결과 역으로 출력
    answer = []
    for j,k in zip(commands,uids):
        if j == 0:
            answer.append(f"{dict_id[k]}님이 들어왔습니다.")
        else:
            answer.append(f"{dict_id[k]}님이 나갔습니다.")

    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))