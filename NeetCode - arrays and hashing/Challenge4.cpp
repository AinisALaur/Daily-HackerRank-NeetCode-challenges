#include<bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<int> static twoSum(vector<int>& nums, int target) {
        map<int, int> number;
        int size = nums.size();

        for(int i = 0; i < size; ++i){
            int remainder = target - nums[i];
            if(number.count(remainder)){
                return vector<int>{number[remainder], i};
            }
            number[nums[i]] = i;
        }

        return vector<int>{-1, -1};
    }
};

int main(){
    vector<int> a = {-3,4,3,90};
    vector<int> sol = Solution::twoSum(a, 0);
    cout<<sol[0]<<" "<<sol[1];



    return 0;
}