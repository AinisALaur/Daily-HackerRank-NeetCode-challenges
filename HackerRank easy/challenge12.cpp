#include<bits/stdc++.h>

using namespace std;

int debounceTimestamps(vector<int> timestamps, int K) {
    int size = timestamps.size();

    if(size <= 0){
        return 0;
    }
    
    int prev = timestamps[0];
    int finalSize = timestamps.size();

    for(int i = 1; i < size; ++i){
        if(timestamps[i] - prev < K){
            --finalSize;
        }else{
            prev = timestamps[i];
        }
    }

    return finalSize;
}

int main(){
    cout<<debounceTimestamps({}, 3)<<endl;
    cout<<debounceTimestamps({1,3,5,8,10}, 3)<<endl;
    cout<<debounceTimestamps({5}, 0)<<endl;

    return 0;
}