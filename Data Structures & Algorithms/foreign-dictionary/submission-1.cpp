class Solution {
public:
    string foreignDictionary(vector<string>& words) {
        unordered_map<char, vector<char>> adj;
        if(not buildAdj(words, adj))
            return "";
        unordered_set<char> visit;
        unordered_set<char> loop;
        vector<char> res;
        for(auto& kv: adj) {
            if(not dfs(kv.first, adj, visit, loop, res))
                return "";
        }
        string r = "";
        for(int i = res.size() - 1; i >= 0; i--) {
            r += res[i];
        }
        return r;
    }

private:
    bool buildAdj(vector<string>& words, unordered_map<char, vector<char>>& adj) {
        for (const string& w : words) {
            for (char c : w) {
                adj[c];  // ensures key exists
            }
        }
        
        int n = words.size();
        for(int i = 0; i < n - 1; i++) {
            string w1 = words[i];
            string w2 = words[i + 1];
            int w1Len = w1.size();
            int w2Len = w2.size();
            if(w1Len > w2Len and w1.substr(0, w2Len) == w2)
                return false;
            
            int j = 0, k = 0;
            while(j < w1Len and k < w2Len and w1[j] == w2[k]) {
                j++;
                k++;
            }
            if(j < w1Len and k < w2Len)
                adj[w1[j]].push_back(w2[k]);
        }
        return true;
    }

    bool dfs(
        char curr,
        unordered_map<char, vector<char>>& adj,
        unordered_set<char>& visit,
        unordered_set<char>& loop,
        vector<char>& res
    ){
        if(loop.count(curr))
            return false;
        if(visit.count(curr))
            return true;
        loop.insert(curr);
        for(auto nei: adj[curr]) {
            if(not dfs(nei, adj, visit, loop, res))
                return false;
        }
        loop.erase(curr);
        visit.insert(curr);
        res.push_back(curr);
        return true;
    }
};
