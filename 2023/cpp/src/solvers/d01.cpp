#include <map>
#include <regex>
#include <sstream>
#include <string>
#include <vector>
#include "d01.h"
#include "solution.h"

Solver01::Solver01() : Solution(1) {}

Solver01::~Solver01() {}

std::string Solver01::part_1(std::string inputs) {
  std::stringstream ss(inputs);
  std::string buffer;

  uint64_t total = 0;
  while (std::getline(ss, buffer, '\n')) {
    std::vector<std::string> found;
    for (auto ch : buffer) {
      int shift = ch - '0';
      if (shift >= 0 && shift < 10) {
        found.push_back(std::string(1, ch));
      }
    }
    std::string number = found.front() + found.back();
    total += std::stoi(number, NULL, 10);
  }

  return std::to_string(total);
}

std::string Solver01::part_2(std::string inputs) {
  std::stringstream ss(inputs);
  std::string buffer;

  std::regex redigits(
      "(?=(one|two|three|four|five|six|seven|eight|nine|zero|\\d))");
  std::map<std::string, int> mapping;
  mapping["one"] = 1;
  mapping["two"] = 2;
  mapping["three"] = 3;
  mapping["four"] = 4;
  mapping["five"] = 5;
  mapping["six"] = 6;
  mapping["seven"] = 7;
  mapping["eight"] = 8;
  mapping["nine"] = 9;
  mapping["zero"] = 0;
  mapping["1"] = 1;
  mapping["2"] = 2;
  mapping["3"] = 3;
  mapping["4"] = 4;
  mapping["5"] = 5;
  mapping["6"] = 6;
  mapping["7"] = 7;
  mapping["8"] = 8;
  mapping["9"] = 9;
  mapping["0"] = 0;

  uint64_t total = 0;
  while (std::getline(ss, buffer, '\n')) {
    std::vector<std::string> found;
    auto search_begin =
        std::sregex_iterator(buffer.begin(), buffer.end(), redigits);
    auto search_end = std::sregex_iterator();

    for (std::sregex_iterator i = search_begin; i != search_end; i++) {
      std::smatch match = *i;
      found.push_back(match.str(1));
    }

    total += 10 * mapping[found.front()] + mapping[found.back()];
  }

  return std::to_string(total);
}
