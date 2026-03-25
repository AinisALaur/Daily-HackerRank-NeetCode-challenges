#include<bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        int size = nums.size();
        vector<int> ans;
        for(int x = 0; x < 2; ++x){
            for(int i = 0; i < size; ++i){
                ans.push_back(nums[i]);
            }
        }

        return ans;
    }
};


int main(){
    Solution sol;
    vector<int> b = {1, 2, 3};
    vector<int> a = sol.getConcatenation(b);

    for(int i : a){
        cout<<i<<" ";
    }


    return 0;
}