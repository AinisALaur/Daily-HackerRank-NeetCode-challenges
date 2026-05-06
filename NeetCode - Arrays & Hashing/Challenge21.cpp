#include<bits/stdc++.h>

using namespace std;

class Solution {
public:
    int static firstMissingPositive(vector<int>& nums) {
        int size = nums.size();
        for(int i = 0; i < size; ++i){
            if(nums[i] < 0){
                nums[i] = 0;
            }
        }

        for(int i = 0; i < size; ++i){
            int index = abs(nums[i]) - 1;
            if(index < 0 || index >= size){
                continue;
            }

            if(nums[index] == 0){
                nums[index] = -1 * (size + 1);
                continue;
            }

            if(nums[index] > 0)
                nums[index] *= -1;
        }

        for(int i = 0; i < size; ++i){
            if(nums[i] >= 0){
                return i + 1;
            }
        }

        return size + 1;

    }
};

int main(){
    vector<int> nums1 = {1, 2, 3, 4, 5, 6};
    vector<int> nums2 = {1, 2, 4, 5, 6};
    vector<int> nums3 = {2, 3, 4, 5, 6};

    cout<<Solution::firstMissingPositive(nums1)<<'\n';
    cout<<Solution::firstMissingPositive(nums2)<<'\n';
    cout<<Solution::firstMissingPositive(nums3)<<'\n';

    return 0;
}