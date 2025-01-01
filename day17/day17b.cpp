
#include <iostream>
#include <vector>
#include <ctime>

int main() {
    int i = 0;
    std::vector<int> instructions = {2, 4, 1, 1, 7, 5, 4, 6, 1, 4, 0, 3, 5, 5, 3, 0};
    std::vector<int> out;
    std::time_t t0 = std::time(nullptr);

    while (true) {
        int A = i;
        int B = 0;
        int C = 0;
        out.clear();

        while (true) {
            B = A % 8;
            B = B ^ 1;
            C = A / (1 << B);
            B = B ^ C;
            B = B ^ 4;
            A = A / (1 << 3);
            out.push_back(B % 8);
            if (out.back() != instructions[out.size() - 1]) {
                break;
            }
            if (A == 0) break;
        }

        if (out == instructions) {
            std::cout << "Found : i = " << i << "  out = {";
            for (int num : out) std::cout << num << " ";
            std::cout << "}" << std::endl;
            break;
        }

        if (i <= 25) {
            std::cout << "i=" << i << " r= { " ;
            for (int num : out) std::cout << num << " ";
            std::cout << "}\n";
        } else {
            break;
        }

        if (i % 40000000 == 0) {
            std::cout << "i = " << i << " " << std::difftime(std::time(nullptr), t0) << "s" << std::endl;
        }

        i++;
    }

    return 0;
}