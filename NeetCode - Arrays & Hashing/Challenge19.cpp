#include<bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<int> static majorityElement(vector<int>& nums) {
        unordered_map<int, int> counts;
        int threshold = nums.size() / 3;

        for(int i : nums){
            counts[i] += 1;

            if(counts.size() == 3){
                unordered_map<int, int> countsTemp;
                for(auto x = counts.begin(); x != counts.end(); ++x){
                    x->second -= 1;
                    if(x->second != 0){
                        countsTemp[x->first] = x->second;
                    }
                }
                counts = countsTemp;
            }
        }

        vector<int> ans;
        for(auto x : counts){
            int count = 0;
            for(int i : nums){
                if(i == x.first){
                    ++count;
                }
            }
            if(count > threshold)
                ans.push_back(x.first);
        }

        return ans;
    }
};

int main(){

    vector<int> nums = {5,2,3,2,2,2,2,5,5,5};
    for(int i : Solution::majorityElement(nums)){
        cout<<i<<" ";
    }


    return 0;
}