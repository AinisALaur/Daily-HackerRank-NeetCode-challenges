#include<bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<int> static topKFrequent(vector<int>& nums, int k) {
        int size = nums.size();
        vector<vector<int>> counts(size);
        unordered_map<int, int> freq;

        for(int i : nums){
            ++freq[i];
        }

        for(auto i : freq){
            counts[i.second - 1].push_back(i.first);
        }

        vector<int> ans;
        for(int i = size - 1; i >= 0; --i){
            if(counts[i].size() != 0){
                for(int x = 0; x < counts[i].size(); ++x){
                    if(ans.size() == k)
                        return ans;

                    ans.push_back(counts[i][x]);
                }
            }    
        }

        return ans;

    }
};

int main(){
    vector<int> nums = {1,1,2,2,3,3,3};
    int k = 3;
    vector<int> ans = Solution::topKFrequent(nums, k);

    for(int i : ans){
        cout<<i<<" "; 
    }

    return 0;
}
