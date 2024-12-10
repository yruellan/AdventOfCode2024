#include <iostream>
#include <fstream>
#include <vector>
#include <tuple>
#include <set>
#include <ctime>
#include <stdlib.h>

using namespace std;

vector<vector<char>> read_input(){
    ifstream file("data6.txt");
    if (!file.is_open()) {
        cerr << "Error opening file" << endl;
        return {};
    }
    vector<vector<char>> input;
    string line;
    while(getline(file, line)){
        vector<char> row;
        for(int i = 0; i < line.size(); i++)
            row.push_back(line[i]);
        input.push_back(row);
    }
    return input;
}

void print_input(vector<vector<char>> data, vector<pair<int,int>> path = {}){
    for(int i = 0; i < data.size(); i++){
        for(int j = 0; j < data[i].size(); j++)
            if (data[i][j] == '^')
                cout << '^';
            else if (find(path.begin(), path.end(), make_pair(i,j)) != path.end())
                cout << '.';
            else if (data[i][j] == '#' || data[i][j] == 'O')
                cout << data[i][j];
            else
                cout << ' ';
        cout << "|" << endl;
    }
    return ;
}

tuple<int,int> get_init(vector<vector<char>> input){
    for(int i = 0; i < input.size(); i++){
        for(int j = 0; j < input[i].size(); j++){
            if( input[i][j] == '^' ){
                input[i][j] = '.';
                return make_tuple(i,j);
            }
        }
    }
    return make_tuple(-1,-1);
}

vector<pair<int,int>> get_path(int i0, int j0,int N, int M, vector<vector<char>> data){
    vector<pair<int,int>> path = vector<pair<int,int>>();

    int dir = 0;

    while (i0 >= 0 && i0 < N && j0 >= 0 && j0 < M){
        if (data[i0][j0] == '.' || data[i0][j0] == '^'){
            path.push_back(make_pair(i0,j0));
            i0 += (dir == 2) - (dir == 0);
            j0 += (dir == 1) - (dir == 3);
        } else if (data[i0][j0] == '#' || data[i0][j0] == 'O'){
            i0 -= (dir == 2) - (dir == 0);
            j0 -= (dir == 1) - (dir == 3);
            dir = (dir + 1) % 4;
            i0 += (dir == 2) - (dir == 0);
            j0 += (dir == 1) - (dir == 3);
        } else {
            cerr << "Error: invalid character in data \'"
                 << data[i0][j0] << "\'\n";
        }
    }

    return path;
}

bool is_valid_obstacle(
    int x, int y, int i0, int j0, vector<vector<char>> data, 
    int N, int M,int *new_path
    ){

    int dir = 0;
    // for (int ind = 0 ; ind < N*M*4 ; ind++)
    //     new_path[ind] = 0;
    for (int ind = 0 ; ind < N*M ; ind++)
        new_path[ind] = 0;

    // while (new_path[i0*M*4+j0*4+dir] == 0){
    while ((new_path[i0*M+j0] & (1 << dir)) == 0){

        // new_path[i0*M*4+j0*4+dir] = 1;
        new_path[i0*M+j0] |= 1 << dir;
        if (data[i0][j0] == '#' || (i0 == x && j0 == y)){
            i0 += (dir == 0) + (dir == 1) - (dir == 2) - (dir == 3);
            j0 += (dir == 0) - (dir == 1) - (dir == 2) + (dir == 3);
            dir = (dir + 1) % 4;
        } else {
            i0 += (dir == 2) - (dir == 0);
            j0 += (dir == 1) - (dir == 3);
        }
        if (i0 < 0 || i0 >= N || j0 < 0 || j0 >= M)
            return false;
    }
    return true;

}

int nb_valid_obstacle(int i0, int j0, int N, int M, vector<vector<char>> data, vector<pair<int,int>> path){

    int x,y ;

    // int *new_path = (int*) malloc(sizeof(int) * N * M * 4);
    // bool *new_path = (bool*) malloc(sizeof(bool) * N * M * 4);
    int *new_path = (int*) malloc(sizeof(int) * N * M);
    
    set<pair<int,int>> valid_obstacles = set<pair<int,int>>();

    for (int k = 1 ; k < path.size(); k++){
        x = path[k].first;
        y = path[k].second;

        if (is_valid_obstacle(x,y,i0,j0,data,N,M,new_path))
            valid_obstacles.insert(make_pair(x,y));
        
    }

    return valid_obstacles.size();
}

int main(){

    vector<vector<char>> data = read_input();
    int N = data.size();
    int M = data[0].size();

    int i0,j0;
    tie(i0,j0) = get_init(data);
    if (i0 == -1){
        cerr << "Error: no initial position found\n";
        return 1;
    }

    // print_input(data);

    cout << "path \n";
    vector<pair<int,int>> path = get_path(i0,j0,N,M,data);

    clock_t start = clock();
    int res = nb_valid_obstacle(i0,j0,N, M, data, path);
    clock_t end = clock();
    double time_taken = double(end - start) / CLOCKS_PER_SEC;
    cout << "Time taken : " << time_taken << "s" << endl;

    // 0.97574s
    
    cout << "path : " << path.size() << "\n";
    cout << "result: " << res << endl;


    return 0;
}