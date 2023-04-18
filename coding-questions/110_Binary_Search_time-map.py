# Source: https://leetcode.com/problems/time-based-key-value-store/

class TimeMap:
    '''
    key -> value(s) at diff. timestamps; retrieve key's value at a certain timestamp
    '''

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # All timestamps are strictly increasing
        # Keys and values are non-empty, and consist of lowercase English letters and digits
        # 1 <= timestamp <= 1E7
        if key not in self.map:
            self.map[key] = ([value],[timestamp])
        else:
            vals, ts = self.map[key]
            vals.append(value)
            ts.append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        # Return lastest value <=  `timestamp` or "" if none exist
        if key not in self.map:
            return ""

        i = self._bisectleft(self.map[key][1], timestamp)
        if i == 0:
            return ""
        else:
            return self.map[key][0][i-1]

    def _bisectleft(self, arr, val):
        assert len(arr) > 0
        N = len(arr)

        i, j = 0, N
        # Invariant: arr[0..i) <= val; arr[j..N) > val; 0 <= i <= j <= N
        while i < j:
            m = (i+j) // 2
            if arr[m] <= val:
                i = m+1
            else:
                j = m
        
        return i



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)