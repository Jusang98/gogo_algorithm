n = int(input())
checker = [list(map(int, input().split())) for _ in range(n)]


x_positions = [arr[0] for arr in checker]
y_positions = [arr[1] for arr in checker]


answer = [-1] * n 


x_positions.sort()
y_positions.sort()


for sx in x_positions:
    for sy in y_positions:
        dist = []
        

        for ex, ey in checker:
            d = abs(ex - sx) + abs(ey - sy)
            dist.append(d)

        dist.sort()
        
        temp = 0
        for i in range(len(dist)):
            d = dist[i]
            temp += d
            if answer[i] == -1: 
                answer[i] = temp
            else: 
                answer[i] = min(temp, answer[i])

print(*answer)
