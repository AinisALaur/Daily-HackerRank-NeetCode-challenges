#include<bits/stdc++.h>

using namespace std;

class Solution {
public:

    string static encode(vector<string>& strs) {
        string ans = "";
        for(string s: strs){
            int length = s.length();
            ans += "#" + to_string(length) + "#";
            ans += s;
        }
        return ans;

    }

    vector<string> static decode(string s) {
        vector<string> ans;
        int size = s.length();
        for(int i = 0; i < size; ++i){
            string number = "";

            if(s[i] == '#'){
                ++i;
                while(isdigit(s[i])){
                    number+=s[i];
                    ++i;
                }
                if(number != "" && s[i] == '#'){
                    int length = stoi(number);
                    string temp = s.substr(i + 1, length);
                    ans.push_back(temp);
                    i += length;
                }
            }
        }
        return ans;
    }
};

int main(){
    vector<string> strs = {"1,23","45,6","7,8,9"};
    vector<string> ans = Solution::decode(Solution::encode(strs));

    for(string s : ans){
        cout<<s<<" ";
    }

    return 0;
}
