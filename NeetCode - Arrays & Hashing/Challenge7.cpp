#include<bits/stdc++.h>

using namespace std;

class Solution {
public:
    int static removeElement(vector<int>& nums, int val) {
        int k = 0;

        for(int i = 0; i <nums.size(); ++i){
            if(nums[i] != val){
                nums[k] = nums[i];
                ++k;
            }
        }

        return k;
    }
};

int main(){
    vector<int> a = {2,3,4,5,6,2,2,7};
    cout<<Solution::removeElement(a, 2)<<endl;

    for(int i : a){
        cout<<i<<" ";
    }

    return 0;
}