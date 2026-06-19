class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        vector<int> maxLeft(n, 0);
        vector<int> maxRight(n, 0);
        for(int i = 1; i < n - 1; i++) {
            maxLeft[i] = max(maxLeft[i-1], height[i-1]);
            maxRight[n - 1 - i] = max(maxRight[n - 1 - (i-1)], height[n - 1 - (i-1)]);
        }

        int res = 0;
        for(int i = 0; i < n; i++) {
            int temp = min(maxLeft[i], maxRight[i]);
            if(temp - height[i] > 0)
                res += temp - height[i];
        }
        return res;
    }
};
