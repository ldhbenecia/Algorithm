import java.util.*;

class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {
        int continuity = 0;
        int lastAttackTime = 0;
        Map<Integer, Integer> attackMap = new HashMap<>();
        int maxHealth = health;
        
        for (int[] attack : attacks) {
            lastAttackTime = Math.max(lastAttackTime, attack[0]);
            attackMap.put(attack[0], attack[1]);
        }
        
        for (int i = 1; i <= lastAttackTime; i++) {
            if (attackMap.containsKey(i)) {
                health -= attackMap.get(i);
                continuity = 0;
                if (health <= 0) {
                    return -1;
                }
            } else {
                continuity++;
                if (continuity < bandage[0]) {
                    health += bandage[1];
                    if (health > maxHealth) {
                        health = maxHealth;
                    }
                } else {
                    health += bandage[1] + bandage[2];
                    continuity = 0;
                    if (health > maxHealth) {
                        health = maxHealth;
                    } 
                }
            }
        }
        
        return health;
    }
}