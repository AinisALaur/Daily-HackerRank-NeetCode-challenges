#include<bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<vector<string>> static groupAnagrams(vector<string>& strs) {
        map<vector<int>, vector<string>> mapping;

        for(string s : strs){
            vector<int> count(26, 0);
            for(char c : s){
                ++count[c - 'a'];
            }
            mapping[count].push_back(s);
        }

        vector<vector<string>> ans;

        for(auto i : mapping){
            ans.push_back(i.second);
        }

        return ans;
    }
};


int main(){
    vector<string> strs = {"act","pots","tops","cat","stop","hat"};
    vector<vector<string>> groups = Solution::groupAnagrams(strs);

    for(int i = 0; i < groups.size(); ++i){
        for(int x = 0; x < groups[i].size(); ++x){
            cout<<groups[i][x]<<" ";
        }cout<<endl;
    }

    return 0;
}