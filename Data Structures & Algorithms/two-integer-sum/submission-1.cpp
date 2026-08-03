class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> ind;
        int n = nums.size();
        for(int i = 0; i < n; i++) {
            if(ind.count(target - nums[i])) {
                return {ind[target - nums[i]], i};
            }
            else
                ind[nums[i]] = i;
        }

        return vector<int>();
    }
};
