function solution(m, n, puddles) {
// puddles 안에 있는 좌표값을 안지나고 가는 최단 경로 개수를 1,000,000,007개로
// 나눈 나머지를 return
    // *1,1부터 시작 
    // 프로그래밍 배열은 행부터 만드는 관습 [n][m]
    let answer = Array.from({length: n+1}, () =>Array(m+1).fill(0))
    answer[1][1] = 1
    // 못지나가는곳은 -1로
    for(let [x,y] of puddles){
        answer[y][x] = -1
    }
    
    for(let i =1; i<= n; i++){
        for(let j = 1; j<=m; j++){
             if(answer[i][j] === -1 ){
                answer[i][j] = 0;
                 continue
            }
            //왼쪽에서 오는길이 있다면 추가
            if(j>1){
            answer[i][j] += answer[i][j-1]
            }
            //위에서 오는 길이 있다면 추가
            if(i>1){
            answer[i][j] += answer[i-1][j]
            }
        answer[i][j] %=1000000007
        }    
    }
    
    return answer[n][m];
}