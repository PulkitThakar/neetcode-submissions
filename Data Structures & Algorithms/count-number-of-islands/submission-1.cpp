class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        int res = 0;
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if(grid[i][j] == '1') {
                    res++;
                    dfs(grid, i, j, m, n);
                }
            }
        }
        return res;
    }

private:
    void dfs(vector<vector<char>>& grid, int i, int j, int m, int n) {
        if (
            i < 0 or i >= m
            or j < 0 or j >= n
            or grid[i][j] != '1'
        )
            return;
        
        grid[i][j] = 'X';
        int delta[][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        for(auto& d: delta) {
            dfs(grid, i + d[0], j + d[1], m, n);
        }
        return;
    }
};
