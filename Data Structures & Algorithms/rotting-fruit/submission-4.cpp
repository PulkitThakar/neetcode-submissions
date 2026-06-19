class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        queue<pair<int, int>> q;
        int count = 0;
        int m = grid.size();
        int n = grid[0].size();
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if(grid[i][j] == 1)
                    count++;
                if(grid[i][j] == 2)
                    q.push({i, j});
            }
        }

        int t = 0;
        while(not q.empty()) {
            int k = q.size();
            int newTime = t + 1;
            while(k > 0) {

                int i = q.front().first;
                int j = q.front().second;
                q.pop();
                
                int delta[][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
                for(auto& d: delta) {
                    int newI = i + d[0];
                    int newJ = j + d[1];
                    if (
                        0 <= newI and newI < m
                        and 0 <= newJ and newJ < n
                        and grid[newI][newJ] == 1
                    ) {
                        grid[newI][newJ] = 2;
                        count--;
                        q.push({newI, newJ});
                        t = newTime;
                        if(count == 0)
                            return t;
                    }
                }
                
                k--;
            }
        }
        return count != 0 ? -1 : t;
    }
};
