#include <bits/stdc++.h>

using namespace std;

int findFirstOccurrence(vector<int> nums, int target) {
    int size = nums.size();
    
    int low = 0;
    int high = size - 1;
    int smallest = -1;
    
    
    while(low <= high){
        int mid = low + (high - low) / 2;

        int number = nums[mid];
        
        if(target == number){
            smallest = mid;
            high = mid - 1;
        }
        
        if(number < target){
            low = mid + 1;
        }

        else if(number > target){
            high = mid - 1;
        }
    }

    return smallest;
}

int main(){


    return 0;
}