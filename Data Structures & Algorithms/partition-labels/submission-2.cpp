class Solution {
public:
    vector<int> partitionLabels(string s) {
        unordered_map<char, int> countMap;
        for(char c: s) {
            countMap[c] += 1;
        }

        int n = s.size();
        int l = 0;
        unordered_set<char> currCharSet;
        vector<int> res;
        for(int r = 0; r < n; r++) {
            if(countMap[s[r]] > 1)
                currCharSet.insert(s[r]);
            countMap[s[r]]--;
            if(countMap[s[r]] == 0)
                currCharSet.erase(s[r]);
            
            if(currCharSet.empty()){
                res.push_back(r - l + 1);
                l = r + 1;
            }
        }
        return res;
        
    }
};
