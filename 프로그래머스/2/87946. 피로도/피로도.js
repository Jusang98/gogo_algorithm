//던전의 순서 한번씩 바꾸는 로직 함수
// 모든 던전 순서 조합(순열)을 생성하는 함수
function generateDungeonOrders(dungeons) {
    const result = [];
    const permute = (arr, current = []) => {
        if (arr.length === 0) {
            result.push([...current]);
            return;
        }
        for (let i = 0; i < arr.length; i++) {
            const rest = [...arr.slice(0, i), ...arr.slice(i + 1)];
            permute(rest, [...current, arr[i]]);
        }
    };
    permute(dungeons);
    return result;
}

function solution(k, dungeons) {
    let maxCount = 0;
    const allOrders = generateDungeonOrders(dungeons); 
    
    for (const order of allOrders) {
        let fatigue = k;
        let count = 0;
        
        for (const [min, use] of order) {
            if (fatigue >= min) {
                fatigue -= use;
                count++;
            } else {
                break; 
            }
        }
        
        maxCount = Math.max(maxCount, count); 
    }
    
    return maxCount;
}