class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        // int slow = nums[0];
        // int fast = nums[nums[0]];
        // while(slow != fast) {
        //     slow = nums[slow];
        //     fast = nums[nums[fast]];
        // }

        // slow = nums[slow];
        // int slow2 = nums[0];
        // while(slow != slow2) {
        //     slow = nums[slow];
        //     slow2 = nums[slow2];
        // }
        // return slow;

        int curr = 0;
        while(nums[curr] > 0) {
            nums[curr] = -1*nums[curr];
            curr = abs(nums[curr]);
        }
        return curr;
    }
};
