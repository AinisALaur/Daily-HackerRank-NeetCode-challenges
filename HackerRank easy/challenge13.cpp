#include<bits/stdc++.h>

using namespace std;

vector<int> findTaskPairForSlot(vector<int> taskDurations, int slotLength) {
    int size = taskDurations.size();
    if(size <= 1){
        return vector<int>{-1, -1};
    }

    map<int, int> remainders;
    for(int i = 0; i < size; ++i){
        if(taskDurations[i] > slotLength)
            continue;
        
        int remainder = slotLength - taskDurations[i];

        if(remainders.count(remainder) == 0){
            remainders[taskDurations[i]] = i;
        }else{
            return vector<int>{remainders[remainder], i};
        }
    }
    return vector<int>{-1, -1};
}

int main(){
    for(int i : findTaskPairForSlot({9,0}, 9)){
        cout<<i<<" ";
    }



    return 0;
}