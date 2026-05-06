#include<bits/stdc++.h>

using namespace std;

class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> prefixes;
        int sum = 0;
        int size = nums.size();
        prefixes[0] = 1;

        int count = 0;

        for(int i = 0; i < size; ++i){
            sum += nums[i];
            count += prefixes[sum - k];
            ++prefixes[sum];
        }

        return count;

    }
};

int main(){


    return 0;
}