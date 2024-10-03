n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = float('-inf')

def recur(idx, price):
    global answer
    if idx == n :
        answer = max(answer, price)
        return
    
    recur(idx + 1 , price)
    if idx + arr[idx][0] <= n:
        recur(idx + arr[idx][0], price + arr[idx][1])
        
recur(0,0)
print(answer)
