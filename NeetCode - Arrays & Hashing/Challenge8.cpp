#include<bits/stdc++.h>

using namespace std;


class Solution {
public:
    int static majorityElement(vector<int>& nums) {
        int count = 1;
        int val = nums[0];

        for(int i = 1; i < nums.size(); ++i){
            if(count == 0){
                val = nums[i];
            }


            if(nums[i] == val){
                ++count;
            }

            else if(nums[i] != val){
                --count;
            }
        }

        return val;


    }
};


int main(){
    vector<int> nums = {5,5,1,1,1,5,5};
    cout<<Solution::majorityElement(nums);


    return 0;
}