function solution(participant, completion) {
    const countMap = new Map();
    
    for (const name of participant) {
        const current = countMap.get(name) ?? 0
        countMap.set(name, current + 1);    
    }
    
    for (const name of completion) {
        const current = countMap.get(name) ?? 0
        if (current >= 1) {
            countMap.set(name, current - 1);
        }
    }
    
    for (const [name, count] of countMap) {
        if (count != 0) {
            return name;   
        }
    }
}