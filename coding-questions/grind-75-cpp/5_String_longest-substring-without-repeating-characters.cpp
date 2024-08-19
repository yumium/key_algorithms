#include <string>
#include <map>

using namespace std;

class Solution {
public:
    /*
        Given:
            s: A string of english letters, digits, symbols and spaces
                0 <= s.size() = N <= 5E4
        
        Return:
            The length of longest substring (consecutive) without repeating characters
        
        Bruteforce:
        Time: O(N^3)
        Space: O(N)

        Current algo
        Time: O(N)
        Space: O(N)

        Obs:
        - Ans >= 1
        - i = 0; j = 1 => s[i..j)
    */
    int lengthOfLongestSubstring(string s) {
        const int N = s.size();
        if (N == 0)
            return 0;

        map<char, int> m {{s[0], 1}}; 
        int max_len = 1;
        int i = 0;    
        int j = 1;   
        bool valid = true;
        while (j < N)
        {
            if (valid) {
                max_len = std::max(max_len, j-i);
                const char c = s[j++];
                if (m.find(c) == m.end()) m[c] = 1;
                else {
                    m[c] = 2;
                    valid = false;
                }
            }
            else {
                const char c = s[i++];
                if (m[c] == 1) m.erase(c);
                else {
                    m[c] = 1;
                    valid = true;
                }
            }
        }
        if (valid) 
            max_len = std::max(max_len, j-i);

        return max_len;
    }
};