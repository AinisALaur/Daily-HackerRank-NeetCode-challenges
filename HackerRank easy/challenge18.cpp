#include <bits/stdc++.h>

using namespace std;

class LargeNum{
    private:    
        vector<char> num;

        vector<char> convert(string number){
            vector<char> temp;
            for(int i = number.length() - 1; i >= 0; --i){
                temp.push_back(number[i]);
            }
            return temp;
        }

    public:
        LargeNum(string number){
            num = convert(number);
        }

        LargeNum add(const LargeNum& number){
            vector<char> num1 = number.num;

            int size1 = num.size();
            int size2 = num1.size();

            int size = max(size1, size2);
            int carry = 0;

            string result;

            for(int i = 0; i < size; ++i){
                int digit1 = (i < size1) ? num[i] - '0' : 0;
                int digit2 = (i < size2) ? num1[i] - '0' : 0;

                int sum = digit1 + digit2 + carry;
                carry = sum / 10;

                result.push_back((sum % 10) + '0');
            }

            if(carry){
                result.push_back(carry + '0');
            }

            reverse(result.begin(), result.end());

            return LargeNum(result);
        }

        string getString(){
            string number = "";
            for(int i = num.size() - 1; i >= 0; --i){
                number+=num[i];
            }
            return number;
        }
};

string countInstallationSequences(int n) {
    if(n == 0){
        return "1";
    }

    if(n == 1){
        return "1";
    }

    LargeNum first("1");
    LargeNum second("1");

    LargeNum current("0");

    for(int i = 2; i <= n; ++i){
        current = first.add(second);
        first = second;
        second = current;
    }

    return current.getString();
}

int main(){
    cout<<countInstallationSequences(1000);

    return 0;
}