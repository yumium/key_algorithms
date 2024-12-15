#include <vector>

using namespace std;

vector<vector<int>> insert_old2(vector<vector<int>>& intervals, vector<int> new_interval) {
    vector<vector<int>> result;
    bool inserted = false;
    for (auto& interval: intervals) {
        if (inserted || interval[1] < new_interval[0]) {
            result.push_back(interval);
        }
        else if (new_interval[1] < interval[0]) {
            result.push_back(new_interval);
            result.push_back(interval);
            inserted = true;
        }
        else {
            new_interval[0] = min(new_interval[0], interval[0]);
            new_interval[1] = max(new_interval[1], interval[1]);
        }
    }
    if (!inserted) {
        result.push_back(new_interval);
    }
    return result;
}
