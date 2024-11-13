N, M  = map(int, input().split())
arr = list(map(int, input().split()))
answer = []

arr.sort()
def recur(number):
    if len(answer) == M:
        print(*answer)
        return
    for i in arr:
        if i in answer:
            continue
        answer.append(i)
        recur(i)
        answer.pop()
        
recur(0)    