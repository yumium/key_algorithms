class Solution {
public:
    /*
        Given:
            grid: M x N grid with cell values in [0, 1, 2]
                1 <= M, N <= 10

        Return:
            # of minute elapse til no cell has fresh orange, or -1 if impossible

        [[2,1,1],
         [0,1,1],
         [1,0,1]]

        Ideas:
        - BFS
            - Start with rotten oranges
            - Do BFS round by round, until list is empty
            - If fresh oranges left, return -1; else return # of rounds - 1
        - TIME: O(M*N)
        - SPACE: O(M*N)
        - Corner:
            - No rotten => init list is empty => minute = 0
            - No fresh => 0
            - No oranges => No rotten
        */
    int orangesRotting(vector<vector<int>>& grid) {
        const int M = grid.size();
        const int N = grid[0].size();
        queue<pair<int, int>> rotten;
        int minutes = 0;

        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (grid[i][j] == 2)
                    rotten.push({i,j});
            }
        }

        step(rotten, grid, M, N);
        while (rotten.size() > 0) {
            minutes += 1;
            step(rotten, grid, M, N);
        }

        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (grid[i][j] == 1)
                    return -1;
            }
        }

        return minutes;
    }

    void step(queue<pair<int, int>>& rotten, vector<vector<int>>& grid, int M, int N) {
        const vector<pair<int, int>> DIR = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        const int len = rotten.size();
        for (int k = 0; k < len; k++) {
            auto [i, j] = rotten.front();
            rotten.pop();

            for (auto [di, dj]: DIR) {
                auto i_new = i+di;
                auto j_new = j+dj;
                if (0 <= i_new && i_new < M && 0 <= j_new && j_new < N && grid[i_new][j_new] == 1) {
                    grid[i_new][j_new] = 2;
                    rotten.push({i_new, j_new});
                }
            }
        }
    }
};