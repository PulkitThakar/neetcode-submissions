class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());
        int n = intervals.size();
        
        int res = 0;
        int temp = intervals[0][1];
        for(int i = 1; i < n; i++) {
            if (intervals[i][0] < temp) {
                res += 1;
                temp = min(temp, intervals[i][1]);
            }
            else
                temp = intervals[i][1];
        }
        return res;
    }
};
