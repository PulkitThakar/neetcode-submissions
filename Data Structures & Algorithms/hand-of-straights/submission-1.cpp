class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        if(hand.size() % groupSize != 0)
            return false;
        priority_queue<int, std::vector<int>, std::greater<int>> pq;
        unordered_map<int, int> m;
        for(int i: hand) {
            pq.push(i);
            m[i] += 1;
        }

        while(!pq.empty()) {
            int start = pq.top(); pq.pop();
            if(m[start] == 0)
                continue;
            
            for(int i = 0; i < groupSize; i++) {
                int k = start + i;
                if(!m.count(k) or m[k] == 0)
                    return false;
                m[k]--;
            }
        }

        return true;
    }
};
