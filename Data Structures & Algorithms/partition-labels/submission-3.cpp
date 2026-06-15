class Solution {
public:
    vector<int> partitionLabels(string s) {
        int n = s.size();
        unordered_map<char, int> lastIndMap;
        for(int i = 0; i < n; i++) {
            lastIndMap[s[i]] = max(i, lastIndMap[s[i]]);
        }

        int l = 0;
        int temp = -1;
        vector<int> res;
        for(int r = 0; r < n; r++) {
            temp = max(temp, lastIndMap[s[r]]);
            if(temp == r){
                res.push_back(r - l + 1);
                l = r + 1;
            }
        }
        return res;
        
    }
};
