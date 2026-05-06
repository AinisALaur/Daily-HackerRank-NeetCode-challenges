#include<bits/stdc++.h>

using namespace std;

class Solution {
public:
    int static longestConsecutive(vector<int>& nums) {
        set<int> newNums;
        int best = 0;

        for(int i : nums){
            newNums.insert(i);
        }

        for(int i : newNums){
            if(newNums.count(i - 1) == 0){
                int count = 1;
                int current = i;
                while(newNums.count(current + 1) == 1){
                    current += + 1;
                    ++count;
                }
                if(count > best){
                    best = count;
                }
            }   
        }
        
        return best;
    }
};

int main(){
    vector<int> nums = {0,3,2,5,4,6,1,1};
    cout<<Solution::longestConsecutive(nums);

    return 0;
}