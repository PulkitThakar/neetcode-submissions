class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        permuteHelper(nums, 0, res);
        return res;
    }
private:
    void permuteHelper(vector<int>& nums, int i, vector<vector<int>>& res) {
        int n = nums.size();
        if(i == n) {
            res.push_back(nums);
            return;
        }
        
        for(int j = i; j < n; j++) {
            swap(nums[i], nums[j]);
            permuteHelper(nums, i + 1, res);
            swap(nums[i], nums[j]);
        }
    }
};