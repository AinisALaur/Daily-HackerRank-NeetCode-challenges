#include<bits/stdc++.h>

using namespace std;

pair<string, int> getPair(string command){
    int gap = command.find(' ');
    if(gap == string::npos){
        return pair<string, int>(command, -1);
    }

    return pair<string, int>(command.substr(0, gap), stoi(command.substr(gap+1, command.length() - gap)));    
}

vector<int> processCouponStackOperations(vector<string> operations) {
    vector<int> stack = {};
    vector<int> returns = {};
    vector<int> minStack = {};
    int min = INT_MAX;
    for(string command : operations){
        pair<string, int> operation = getPair(command);

        if(operation.first == "push"){
            int x = operation.second;
            stack.push_back(x);
            if(x < min){
                min = x;
            }
            minStack.push_back(min);
        }

        if(operation.first == "getMin"){
            returns.push_back(minStack.back());
        }

        if(operation.first == "top"){
            returns.push_back(stack.back());
        }

        if(operation.first == "pop"){
            stack.pop_back();
            minStack.pop_back();
        }
    }   

    return returns;
}

int main(){
    vector<string> a = {"push 1", "push 0", "getMin", "pop", "getMin"};
    for(auto i : processCouponStackOperations(a))
        cout<<i<<" ";


    return 0;
}