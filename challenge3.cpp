#include <bits/stdc++.h>
#include <algorithm>

using namespace std;

int binarySearch(vector<int> nums, int target) {
    int size = nums.size();
    
    int low = 0;
    int high = size - 1;
    
    while(low <= high){
        int mid = low + (high - low) / 2;

        int number = nums[mid];
        
        if(target == number){
            return mid;
        }
        
        if(number < target){
            low = mid + 1;
        }

        else if(number > target){
            high = mid - 1;
        }
    }

    return -1;
}

int main(){
    srand(time(0));
    int size = 5;
    vector<int> nums = {};
    set<int> areInside;

    for(int i = 0; i < size; ++i){
        int randomNum = rand() % 101;
        nums.push_back(randomNum);
        areInside.insert(randomNum);
    }

    sort(nums.begin(), nums.end());

    for(auto i : areInside){
        cout<<binarySearch(nums, i)<<endl;
    }

    cout<<binarySearch(nums, -1)<<endl;

    return 0;
}
