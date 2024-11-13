def recur(number):
    if len(arr) == M:
        print(*arr) 
        return
    for i in range(number, N+1):
        arr.append(i)
        recur(i)
        arr.pop()
N, M = map(int, input().split())
arr = []
recur(1)