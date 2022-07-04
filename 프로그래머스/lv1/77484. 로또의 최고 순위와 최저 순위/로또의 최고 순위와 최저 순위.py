def solution(lottos, win_nums):
    answer = []
    zeroCnt, lucky = 0, 0

    for i in lottos :
        if 0 == int(i) :
            zeroCnt += 1

    for i in range(len(win_nums)) :
        for j in range(len(win_nums)) :
            if win_nums[i] == lottos[j] :
                lucky += 1


    SumList = [lucky+zeroCnt, lucky]
    for i in SumList :
        if i == 6:
            answer.append(1)
        elif i == 5:
            answer.append(2)
        elif i == 4:
            answer.append(3)
        elif i == 3:
            answer.append(4)
        elif i == 2:
            answer.append(5)
        else:
            answer.append(6)
    print(answer)
    return answer
