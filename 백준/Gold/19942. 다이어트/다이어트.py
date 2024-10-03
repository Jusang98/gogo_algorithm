n = int(input())
A, B, C, D = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
answer = 9999999999
select_foods = []
def recur(idx, a, b, c, d, price, selected):
    global answer, select_foods
    if idx == n:
        if a >= A and b >= B and c >= C and d >= D:
            if answer > price:
                select_foods = selected[:]
                answer = price
            elif answer == price:
                select_foods = min(select_foods, selected)
        return
    recur(idx+1, a + arr[idx][0], b + arr[idx][1], c + arr[idx][2], d + arr[idx][3], price + arr[idx][4], selected + [idx+1])
    
    recur(idx+1, a, b ,c, d, price, selected)
recur(0,0,0,0,0,0,[])

if answer == 9999999999:
    print(-1)
else: 
    print(answer)
    print(*select_foods)
    # print(" ".join(map(str, select_foods)))