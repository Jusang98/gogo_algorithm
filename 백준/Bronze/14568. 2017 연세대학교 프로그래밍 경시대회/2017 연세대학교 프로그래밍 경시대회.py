n = int(input())
answer = 0
for a in range(0, n+1):
    for b in range(0, n+1):
        for c in range(0, n+1):    
            
            if a + b + c == n and c >= b+2 and a % 2 == 0 and a !=0 and b != 0 and c != 0:
                answer += 1
print(answer)