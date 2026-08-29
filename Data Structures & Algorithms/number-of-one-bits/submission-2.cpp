class Solution {
public:
    int hammingWeight(uint32_t n) {
        uint32_t mask = 1;
        int res = 0;
        while(n > 0) {
            res += (n & mask);
            n = n >> 1;
        }
        return res;
    }
};
