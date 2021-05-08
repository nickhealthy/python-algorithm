def solution(record):
    answer = []
    idmap = {}
    
    for s in record:
        strlist = s.split()
        cmd = strlist[0]
        if cmd == "Enter" or cmd == "Change":
            id = strlist[1]
            name = strlist[2]
            idmap[id] = name
    
    for s in record:
        strlist = s.split()
        cmd = strlist[0]
        id = strlist[1]
        if cmd == "Enter":
            answer.append(idmap[id] + "님이 들어왔습니다.")
        if cmd == "Leave":
            answer.append(idmap[id] + "님이 나가셨습니다.")
    return answer