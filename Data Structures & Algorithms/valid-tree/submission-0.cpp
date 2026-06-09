class Solution {
public:
    bool validTree(int n, vector<vector<int>>& edges) {
        vector<int> rank(n, 1);
        vector<int> par;
        for(int i = 0; i < n; i++)
            par.push_back(i);
        
        for(auto& edge: edges) {
            if(unionFunc(par, rank, edge[0], edge[1]))
                return false;
        }
        
        for(int i = 0; i < n; i++)
            findFunc(par, i);
        
        for(int i = 0; i < n-1; i++)
            if(par[i] != par[i+1])
                return false;
        return true;
    }

private:
    bool unionFunc(vector<int>& par, vector<int>& rank, int n1, int n2) {
        int p1 = findFunc(par, n1);
        int p2 = findFunc(par, n2);

        if(p1 == p2)
            return true;
        
        if(rank[p1] >= rank[p2]) {
            rank[p1] += rank[p2];
            par[p2] = p1;
        } else {
            rank[p2] += rank[p1];
            par[p1] = p2;
        }
        return false;
    }
    int findFunc(vector<int>& par, int n) {
        if(n != par[n])
            par[n] = findFunc(par, par[n]);
        return par[n];
    }
};
