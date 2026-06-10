class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int l = 1, r = std::ranges::max(piles);
        int res = r;
        while(l <= r) {
            int m = l + ((r - l)/2);
            int t = consumeTime(piles, m);
            if(t > h)
                l = m + 1;
            else{
                res = m;
                r = m - 1;
            }
        }
        return res;
    }

private:
    int consumeTime(vector<int>& piles, int r) {
        int res = 0;
        for(int p: piles) {
            res += ((p + r - 1)/r);
        }
        return res;
    }
};
