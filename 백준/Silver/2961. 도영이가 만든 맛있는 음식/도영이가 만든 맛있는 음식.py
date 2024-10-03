n = int(input())
flavor = [list(map(int,input().split())) for _ in range(n)]
answer = 9999999999
def recur(idx, ssin, ssen,used):
    global answer
    if idx == n:
        if used:
            result = abs(ssin - ssen)
            answer = min(answer, result)
        return
    recur(idx+1,ssin * flavor[idx][0], ssen + flavor[idx][1],True)

    recur(idx+1, ssin, ssen,used)
recur(0,1,0, False)
print(answer)