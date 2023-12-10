#include <string>
#include <iostream>
#include <sstream>
#include <fstream>
#include "registry.h"

void usage(std::string name) {
    std::cerr << "./" << name << " <day> <input file> {1,2,all}" << std::endl;
}

int main(int argc, char* argv[]) {
    if (argc != 3 && argc != 4) {
        usage(argv[0]);
        return 1;
    }

    Registry days {};

    int day = std::stoi(argv[1]);
    std::string filename = argv[2];
    int part {0};
    if (argc == 4) {
        part = std::stoi(argv[3]);
    }

    Solution* solver = days.get_solver(day);
    if (!solver) {
        std::cerr << "ERROR: solver for day #" << day << " not found" << std::endl;
        return 2;
    }

    std::ifstream fp(filename);
    std::stringstream inputs {};
    inputs << fp.rdbuf();

    std::cout << "Day #" << day << std::endl;
    if (part == 0 || part == 1) {
        std::cout << "Part #1: " << solver->part_1(inputs.str()) << std::endl;
    }
    if (part == 0 || part == 2) {
        std::cout << "Part #2: " << solver->part_2(inputs.str()) << std::endl;
    }

    return 0;
}
