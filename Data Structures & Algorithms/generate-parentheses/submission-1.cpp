class Solution {
public:
    vector<string> generateParenthesis(int n) {
        string s = "";
        vector<string> res;
        backtracking(n, 0, 0, s, res);
        return res;
    }

private:
    void backtracking(int n, int o, int c, string& s, vector<string>& res) {
        if(o == n and c == n) {
            res.push_back(s);
            return;
        }
        
        if(o < n) {
            s.push_back('(');
            backtracking(n, o + 1, c, s, res);
            s.pop_back();
        }

        if(c < o) {
            s.push_back(')');
            backtracking(n, o, c + 1, s, res);
            s.pop_back();
        }
    }
};
