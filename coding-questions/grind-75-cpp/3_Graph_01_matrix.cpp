using namespace std;

class Solution {
public:
    /*
        Given:
            mat: Array of binary digits
                1 <= M, N <= 1E4
                1 <= M*N <= 1E4
                Exist i,j s.t. mat[i][j] = 0            

        Return:
            Matrix of same size, res[i][j] = distance to closest 0 from cell

        Obs:
        - In result matrix, every cell is defined
        - 0 <= res[i][j] <= M+N-2

        Bruteforce: 
        Time: O((M*N)^2)
        Space: O(M*N)

        Time: O(M*N)
        Space: O(M*N)
    */
    vector<vector<int>> updateMatrix(vector<vector<int>>& mat) {
    vector<int> DIR = {0, 1, 0, -1, 0};
        int m = mat.size(), n = mat[0].size();
        queue<pair<int, int>> q;
        for (int r = 0; r < m; ++r)
            for (int c = 0; c < n; ++c)
                if (mat[r][c] == 0) q.emplace(r, c);
                else mat[r][c] = -1; // Marked as not processed yet!

        while (!q.empty()) {
            auto [r, c] = q.front(); q.pop();
            for (int i = 0; i < 4; ++i) {
                int nr = r + DIR[i], nc = c + DIR[i+1];
                if (nr < 0 || nr == m || nc < 0 || nc == n || mat[nr][nc] != -1) continue;
                mat[nr][nc] = mat[r][c] + 1;
                q.emplace(nr, nc);
            }
        }
        return mat;
    }
};