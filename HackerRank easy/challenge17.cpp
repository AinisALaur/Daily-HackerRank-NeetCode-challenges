#include <bits/stdc++.h>

using namespace std;

long getAutoSaveInterval(int n) {
    long first = 1;
    long second = 2;

    if(n == 0){
        return first;
    }

    if(n == 1){
        return second;
    }

    long current;
    for(int i = 2; i <= n; ++i){
        current = first + second;
        first = second;
        second = current;
    }

    return current;
}

int main(){
    cout<<getAutoSaveInterval(10);

    return 0;
}