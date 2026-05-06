#include<bits/stdc++.h>

using namespace std;

class Solution {
public:
    string static longestCommonPrefix(vector<string>& strs) {
        int size = strs.size();
        int sizeOfFirst = strs[0].size();
        string prefix = "";
        for(int i = 0; i < sizeOfFirst; ++i){
            char letter = strs[0][i];
            for(int x = 1; x < size; ++x){
                if(i >= strs[x].size() || letter != strs[x][i]){
                    return prefix;
                }
            }
            prefix += letter;
        }
        return prefix;
    }
};

int main(){
    vector<string> a = {"a","a","a"};
    cout<<Solution::longestCommonPrefix(a);
    return 0;
}