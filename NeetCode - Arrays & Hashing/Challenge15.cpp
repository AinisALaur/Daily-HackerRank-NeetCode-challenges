#include<bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<int> static productExceptSelf(vector<int>& nums) {
        vector<int> ans;
        int size = nums.size();
        vector<int> prefix(size + 1, 1);
        vector<int> suffix(size + 1, 1);

        int j = size - 1;
        int preProd = 1;
        int sufProd = 1;

        for(int i = 0; i < size; ++i){

            preProd *= nums[i];
            sufProd *= nums[j];

            prefix[i + 1] = preProd;
            suffix[j] = sufProd;
            --j;
        }

        for(int i = 1; i <= size; ++i){
            ans.push_back(prefix[i - 1] * suffix[i]);
        }

        return ans;
    }
};

int main(){
    vector<int> arr = {1, 2, 4, 6};
    vector<int> ans = Solution::productExceptSelf(arr);

    for(int i : ans){
        cout<<i<<" ";
    }


    return 0;
}