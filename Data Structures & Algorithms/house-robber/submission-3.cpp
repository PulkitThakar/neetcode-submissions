class Solution {
public:
    int rob(vector<int>& nums) {
        int last = 0, prev = 0;

        for(int i: nums) {
            int temp = max(prev + i, last);
            prev = last;
            last = temp;
        }

        return last;
    }
};
