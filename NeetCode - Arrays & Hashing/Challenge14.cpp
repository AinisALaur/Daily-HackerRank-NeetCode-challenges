#include<bits/stdc++.h>

using namespace std;


class NumMatrix {
private:
    vector<vector<int>> sumMatrix;

public:
    NumMatrix(vector<vector<int>>& matrix) {
        int n = matrix.size();
        int m = matrix[0].size();
        sumMatrix = vector<vector<int>>(n + 1, vector<int>(m + 1, 0));

        for(int i = 1; i < n + 1; ++i){
            int rowSum = 0;
            for(int x = 1; x < m + 1; ++x){
                rowSum += matrix[i - 1][x - 1];
                sumMatrix[i][x] = rowSum + sumMatrix[i - 1][x];
            }
        }
    }

    int sumRegion(int row1, int col1, int row2, int col2) {
        int sum = sumMatrix[row2 + 1][col2 + 1];
        sum -= sumMatrix[row1][col2 + 1];
        sum -= sumMatrix[row2 + 1][col1];
        sum += sumMatrix[row1][col1];
        return sum;
    }
    
};

int main(){
    vector<vector<int>> mat = {
        {3, 0, 1, 4, 2},
        {5, 6, 3, 2, 1},
        {1, 2, 0, 1, 5},
        {4, 1, 0, 1, 7},
        {1, 0, 3, 0, 5}
    };

    NumMatrix matrix(mat);
    cout<<matrix.sumRegion(2, 1, 4, 3);


    return 0;
}