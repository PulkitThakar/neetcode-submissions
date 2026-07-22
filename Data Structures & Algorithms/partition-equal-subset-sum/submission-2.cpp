class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int s = accumulate(nums.begin(), nums.end(), 0);
        if(s%2 == 1)
            return false;
        
        int n = s / 2;

        vector<bool> dp(n + 1, false);
        dp[0] = true;

        for(int i : nums) {
            for(int j = n; j >= i; j--) {
                if(dp[j - i])
                    dp[j] = true;
            }
            if(dp[n])
                return true;
        }
        return false;
    }
};
