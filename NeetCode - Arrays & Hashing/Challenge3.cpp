#include<bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool static isAnagram(string s, string t) {
        int size1 = s.length();
        int size2 = t.length();

        unordered_map<char, int> chars1;

        if(size1 != size2){
            return false;
        }

        for(int i = 0; i < size1; ++i){
            ++chars1[s[i]];
            --chars1[t[i]];
        }

        for(auto i : chars1){
            if(i.second != 0){
                return false;
            }
        }

        return true;
    }
};

int main(){

    cout<<Solution::isAnagram("racecar", "carrace");


    return 0;
}