#include <vector>
#include <iostream>
#include <format>

using namespace std;

class Solution {
public:
    /*
        Given:
            points: A vector of points
            k: # of closest points to origin (0,0) to return
                1 <= k <= points.size() = N <= 1E4
                -1E4 <= points[i][0], points[i][1] <= 1E4

        Return:
            A vector of k closest points to origin. Return in any order, guaranteed to be unique
                Distance to origin is Euclidean

        Idea 1: Sort and return points[0..k)
        Time: O(N log N)
        Space: O(1) <- sorting in-place

        Idea 2: Random select 
        Time: O(N)
        Space: O(1) <- partition is in-place
    */
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        selectK(points, 0, points.size(), k);
        points.resize(k);
        return points;
    }

    void selectK(vector<vector<int>>& points, int i, int j, int k)
    {
        // std::format("i = {}, j = {}, k = {}", i, j, k);
        auto part = partition3(points, i, j);
        int l = part[0];
        int r = part[1];

        // points[i..l) ++ points[l..r) ++ points[r..j)
        if ((l-i) >= k)
            selectK(points, i, l, k);
        else if ((r-i) < k)
            selectK(points, r, j, k-(r-i));
    }

    vector<int> partition3(vector<vector<int>>& points, int l, int r)
    {
        const int val = dist(points[l][0], points[l][1]);
        int i = l+1;
        int j = l+1;
        int k = r;

        // Invariant: points[l+1..i) < val; points[i..j) = val; points[k..r) > val; l+1 <= i <= j <= k <= r
        while (j < k)
        {
            const int d = dist(points[j][0], points[j][1]);
            if (d < val)
            {
                swap(points, i, j);
                i++;
                j++;
            }
            else if (d == val)
                j++;
            else
            {
                k--;
                swap(points, j, k);
            }
        }

        swap(points, l, i-1);
        vector<int> res {l, i-1};
        return res;
    }

    int dist(int x, int y)
    {
        return x*x + y*y;
    }

    void swap(vector<vector<int>>& points, int i, int j)
    {
        auto temp_x = points[i][0];
        auto temp_y = points[i][1];

        points[i][0] = points[j][0];
        points[i][1] = points[j][1];

        points[j][0] = temp_x;
        points[j][1] = temp_y;
    }
};



int main()
{
    Solution sol;
    vector<vector<int>> vec {{1,3} ,{-2,2}};
    auto ans = sol.kClosest(vec, 1);
    std::cout << "Size is: " << ans.size() << ans[0][0] << ", " << ans[0][1] << std::endl;
}