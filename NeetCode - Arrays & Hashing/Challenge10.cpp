#include<bits/stdc++.h>

using namespace std;

class Solution {
private:
    int medianOfThree(vector<int>& arr, int low, int high) {
        int mid = low + (high - low) / 2;

        if (arr[low] > arr[mid]) swap(arr[low], arr[mid]);
        if (arr[low] > arr[high]) swap(arr[low], arr[high]);
        if (arr[mid] > arr[high]) swap(arr[mid], arr[high]);

        swap(arr[mid], arr[high]);

        return arr[high];
    }

int partition(vector<int>& arr, int low, int high) {
    int pivot = medianOfThree(arr, low, high);
    int i = low - 1;

    for (int j = low; j < high; j++) {
        if (arr[j] < pivot) {
            i++;
            if(i != j)
                swap(arr[i], arr[j]);
        }
    }
    
    swap(arr[i + 1], arr[high]);  
    return i + 1;
}

void quickSort(vector<int>& arr, int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

public:
    vector<int> sortArray(vector<int>& nums) {
        quickSort(nums, 0, nums.size() - 1);
        return nums;
    }
};



int main(){
    vector<int> nums = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0};
    Solution sol;
    sol.sortArray(nums);
    for(int i : nums){
        cout<<i<<" ";
    }

    return 0;
}