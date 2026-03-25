#include<bits/stdc++.h>

using namespace std;


class Solution {
public:
    bool static hasDuplicate(vector<int>& nums) {
        set<int> contains;
        int size = nums.size();
        for(int i = 0; i < size; ++i){
            if(contains.count(nums[i]) == 0){
                contains.insert(nums[i]);
            }else{
                return true;
            }
        }
        return false;
    }
};

int main(){
    vector<int> test = {1, 2, 3, 4, 5, 5};
    cout<<Solution::hasDuplicate(test);

    return 0;
}