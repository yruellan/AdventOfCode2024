
#include <iostream>
#include <vector>
#include <chrono>
#include <cmath>

using namespace std;
using namespace std::chrono;

int64_t A = 0;
int64_t B = 0;
int64_t C = 0;
vector<int> instructions = {2, 4, 1, 1, 7, 5, 4, 6, 1, 4, 0, 3, 5, 5, 3, 0};
// vector<int> instructions = {0,3,5,4,3,0};
// vector<int> instructions = {0,1,5,4,3,0};

vector<int> run_op(int64_t A, int64_t B, int64_t C, const vector<int>& instructions) {
    vector<int> out;
    int IP = 0;

    while (IP < instructions.size()) {
        int opcode = instructions[IP];
        int operand = instructions[IP + 1];

        int64_t combo_op = operand;

        if (operand == 4) combo_op = A;
        else if (operand == 5) combo_op = B;
        else if (operand == 6) combo_op = C;
        else if (operand == 7) throw invalid_argument("Invalid operand");

        if (opcode == 0) {
            A = A / (1 << combo_op);
        } else if (opcode == 1) {
            B = B ^ operand;
        } else if (opcode == 2) {
            B = combo_op % 8;
        } else if (opcode == 3) {
            if (A != 0) {
                IP = operand - 2;
            }
        } else if (opcode == 4) {
            B = B ^ C;
        } else if (opcode == 5) {
            out.push_back(combo_op % 8);
            if (out.back() != instructions[out.size() - 1]) {
                return {};
            }
        } else if (opcode == 6) {
            B = A / (1 << combo_op);
        } else if (opcode == 7) {
            C = A / (1 << combo_op);
        }

        IP += 2;
    }
    return out;
}

int main() {
    auto t0 = high_resolution_clock::now();
    int64_t i = 0;
    vector<int> r = {};
    while (true) {

        r = run_op(i, B, C, instructions);
        if (instructions == r) {
            cout << "Foud : i=" << i << " r= { " ;
            for (int num : r) cout << num << " ";
            cout << "}\n";
        }
        // break;

        // if (i <= 64 + 10) {
        //     cout << "i=" << i << " r= { " ;
        //     for (int num : r) cout << num << " ";
        //     cout << "}" << endl;
        // } 
        // else break;
        

        if (i % 4000000 == 0) {
            auto t1 = high_resolution_clock::now();
            duration<double> elapsed = t1 - t0;
            cout << "i = " << i << " " ;
            int64_t total = 1UL << 48;
            cout << " " << i / total << "% " ;
            cout << " log : " << log2(i) << " " ;
            cout << elapsed.count() << "s" << endl;
        }

        i += 1;
    }
    return 0;
}