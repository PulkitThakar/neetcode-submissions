class Solution {
public:
    int trap(vector<int>& height) {
        int maxLeft = 0;
        int maxRight = 0;
        int i = 0;
        int j = height.size() - 1;
        int res = 0;
        while(i <= j) {
            int temp = min(maxLeft, maxRight);
            if(maxLeft <= maxRight) {
                int tempRes = temp - height[i];
                if(tempRes > 0)
                    res += tempRes;
                maxLeft = max(height[i], maxLeft);
                i++;
            }
            else {
                int tempRes = temp - height[j];
                if(tempRes > 0)
                    res += tempRes;
                maxRight = max(height[j], maxRight);
                j--;
            }
        }
        return res;
    }
};
