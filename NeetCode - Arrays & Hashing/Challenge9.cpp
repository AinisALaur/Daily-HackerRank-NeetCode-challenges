#include<bits/stdc++.h>

using namespace std;

class MyHashSet {
private:
    vector<int> arr;
    int capacity;
    int size;

    int hashCode(int val){
        return val % capacity;
    }

public:
    MyHashSet() {
        size = 0;
        capacity = 20029; // big enough prime number
        arr = vector<int>(capacity, -1);
    }
    
    void add(int key) {
        int index = hashCode(key);
    
        if(contains(key)){
            return;
        }
        
        int i = 1;
        while(arr[index] != -1){
            index = (index + i*i) % capacity;
            ++i;
        }

        arr[index] = key;
    }
    
    void remove(int key) {
        int index = hashCode(key);
        int start = index;
        int i = 1;
        while(arr[index] != key){
            if(arr[index] == -1){
                return;
            }

            index = (index + i*i) % capacity;
            ++i;

            if(index == start){
                return;
            }
        }
        arr[index] = - 1;
    }
    
    bool contains(int key) {
        int index = hashCode(key);
        int start = index;
        int i = 1;
        while(arr[index] != key){
            if(arr[index] == -1){
                return false;
            }
            index = (index + i*i) % capacity;
            ++i;
            if(index == start){
                return false;
            }
        }
        return true;
    }
};

int main(){
    MyHashSet hashset;
    for(int i = 0; i <= 10000; ++i){
        hashset.add(i);
    }

    for(int i = 0; i <= 10000; ++i){
        hashset.remove(i);
    }

    for(int i = 0; i <= 10000; ++i){
        if(hashset.contains(i) != 0){
            cout<<"Error"<<endl;
        }
    }
    
    return 0;
}