#include <iostream>
#include <algorithm>
#include <map>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int answer = 0;
        int ind = 0;
        map<char, int> indexes;
        
        for (int i = 0; i < s.length(); ++i) { 
            if (indexes.find(s[i]) != indexes.end() && indexes[s[i]] >= ind) {
                answer = max(answer, i - ind);
                ind = indexes[s[i]] + 1; 
            }
            indexes[s[i]] = i; 
        }
        
        return max(answer, static_cast<int>(s.length()) - ind); 
    }
};
