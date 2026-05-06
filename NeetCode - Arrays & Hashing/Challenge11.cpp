#include<bits/stdc++.h>

using namespace std; 

class Solution {
public:
    void static sortColors(vector<int>& nums) {
        int l = 0;
        int r = nums.size() - 1;

        int i = 0;
        while(i <= r){
            if(nums[i] == 0){
                swap(nums[i], nums[l]);
                ++l;
            }

            if(nums[i] == 2){
                swap(nums[i], nums[r]);
                --r;
                --i;
            }

            ++i;
        }
    
    }
};

int main(){
    vector<int> colors = {0,1,2,2,1,2,1,0,2,1,2,0,1,2};
    Solution::sortColors(colors);

    for(int i : colors){
        cout<<i<<" ";
    }

    return 0;
}