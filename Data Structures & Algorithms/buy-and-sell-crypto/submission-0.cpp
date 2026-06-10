class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        if(n == 1)
            return 0;
        
        int res = 0;
        int l = 0;
        for(int r = 1; r < n; r++) {
            int temp = prices[r] - prices[l];
            if(temp < 0)
                l = r;
            else
                res = max(res, temp);
        }
        return res;
    }
};
