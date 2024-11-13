N,M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
arr = [] 
def recur(number):
    if len(arr) == M:
        print(*arr)
        return
    for i in nums:
        arr.append(i)
        recur(i)
        arr.pop()
recur(0)        