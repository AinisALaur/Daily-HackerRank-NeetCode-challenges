#include<bits/stdc++.h>

using namespace std;

class MyHashMap {
private:
    int capacity;
    vector<pair<int, int>> arr;

    int hash(int key){
        return key % capacity;
    }

public:
    MyHashMap() {
        capacity = 10007;
        arr = vector<pair<int, int>>(capacity, pair<int, int>(-1, -1));
    }
    
    void put(int key, int value) {
        int index = hash(key);
        int i = 1;

        while(arr[index].second != -1 && arr[index].first != key){
            index = (index + i * i) % capacity;
            ++i;
        }

        arr[index] = pair<int, int>(key, value);
    }
    
    int get(int key) {
        int index = hash(key);
        int i = 1;
        int start = index;
        while(arr[index].first != key){
            index = (index + i * i) % capacity;
            ++i;

            if(index == start){
                return -1;
            }

        }
        return arr[index].second;
    }
    
    void remove(int key) {
        int index = hash(key);
        int i = 1;
        int start = index;
        while(arr[index].first != key){
            index = (index + i * i) % capacity;
            ++i;

            if(index == start){
                return;
            }
        }
        arr[index] = pair<int, int>(-1, -1);
    }
};

int main(){
    MyHashMap *map = new MyHashMap();
    map->put(1, 1);
    map->put(2, 2);
    cout<<map->get(1)<<'\n';
    cout<<map->get(3)<<'\n';
    map->put(2, 1);
    cout<<map->get(2)<<'\n';
    map->remove(2);
    cout<<map->get(2)<<'\n';
    return 0;
}