N, M  = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
answer = []


def recur(number):
    if len(answer) == M:
        print(*answer)
        return
    for i in range(number, len(arr)):
        # if arr[i] not in answer:
        #     continue
        answer.append(arr[i])
        recur(i + 1)
        answer.pop()
recur(0)