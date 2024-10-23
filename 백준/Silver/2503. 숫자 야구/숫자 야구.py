n = int(input())
hint = [list(map(int, input().split())) for _ in range(n)]
answer = 0

for a in range(1,10):
    for b in range(1, 10):
        if a == b :
            continue
        for c in range(1, 10):
            if a == c or b == c:
             continue
            
            
            cnt = 0
            for arr in hint:
                number = arr[0]
                strike = arr[1]
                ball = arr[2]
                d = number // 100
                e = (number % 100) // 10
                f = number % 10 
                strike_cnt = 0
                ball_cnt = 0    
                
                if a == d:
                    strike_cnt += 1
                if b == e:
                    strike_cnt += 1
                if c == f:
                    strike_cnt += 1
                    
                if a == e or a == f:
                    ball_cnt += 1
                if b == d or b == f:
                    ball_cnt += 1
                if c == d or c == e:
                    ball_cnt += 1   
                       
                if strike_cnt == strike and ball_cnt == ball:
                    cnt += 1
            if cnt == n:
                answer += 1
print(answer)     
            #abc랑 number랑 비교해서 strike랑 볼 카운트가 맞는지 확인 맞으면 다음 arr의 number도 다확인 strike랑 볼카운트 확인 맞으면 answer +=1