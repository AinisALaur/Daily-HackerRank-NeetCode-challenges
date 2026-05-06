#include<bits/stdc++.h>

using namespace std;

#define boardSize 9

class Solution {
private:
    bool static checkRowsNCols(vector<vector<char>>& board, int startRow, int endRow, int startCol, int endCol, int renew){
        vector<int> rowCounts(boardSize, 0);
        vector<int> colCounts(boardSize, 0);

        for(int i = startRow; i < endRow; ++i){
            if(i % renew == 0){
                rowCounts = vector<int>(boardSize, 0);
                colCounts = vector<int>(boardSize, 0);
            }

            for(int x = startCol; x < endCol; ++x){
                
                int cellRow = (board[i][x] - '0') - 1;
                int cellCol = (board[x][i] - '0') - 1;


                if(board[i][x] != '.' && rowCounts[cellRow] > 0){
                    return false;
                }

                if(board[x][i] != '.' && colCounts[cellCol] > 0){
                    cout<<board[x][i]<<" ";
                    return false;
                }
                
                if(board[i][x] != '.')
                    ++rowCounts[cellRow];

                if(board[x][i] != '.')
                    ++colCounts[cellCol];
            }
        }

        return true;
    }


public:
    bool static isValidSudoku(vector<vector<char>>& board) {
        if(!checkRowsNCols(board, 0, 9, 0, 9, 1)){
            return false;
        }

        //check squares
        for(int i = 0; i < boardSize / 3; ++i){
            int startRow = 3*i;
            int endRow = (3 * (i + 1));
            for(int x = 0 ; x < boardSize / 3; ++x){
                int startCol = 3*x;
                int endCol = (3 * (x + 1));

                if(!checkRowsNCols(board, startRow, endRow, startCol, endCol, 3)){
                    return false;
                }
            }   
        }

        return true;
    }
};


int main(){
    vector<vector<char>> board =
        {{'1','2','.','.','3','.','.','.','.'},
        {'4','.','.','5','.','.','.','.','.'},
        {'.','9','8','.','.','.','.','.','3'},
        {'5','.','.','.','6','.','.','.','4'},
        {'.','.','.','8','.','3','.','.','5'},
        {'7','.','.','.','2','.','.','.','6'},
        {'.','.','.','.','.','.','2','.','.'},
        {'.','.','.','4','1','9','.','.','8'},
        {'.','.','.','.','8','.','.','7','9'}};

    // vector<vector<char>> board =
        // {{'1','2','.','.','3','.','.','.','.'},
        // {'4','.','.','5','.','.','.','.','.'},
        // {'.','9','1','.','.','.','.','.','3'},
        // {'5','.','.','.','6','.','.','.','4'},
        // {'.','.','.','8','.','3','.','.','5'},
        // {'7','.','.','.','2','.','.','.','6'},
        // {'.','.','.','.','.','.','2','.','.'},
        // {'.','.','.','4','1','9','.','.','8'},
        // {'.','.','.','.','8','.','.','7','9'}};


    cout<<Solution::isValidSudoku(board);

    return 0;
}