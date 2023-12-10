#include <iostream>
#include <regex>
#include <sstream>
#include <string>
#include <vector>
#include "d02.h"
#include "solution.h"

int find_maximum_value_given_regex(std::regex re, std::string line) {
  int max = 0;
  auto search_begin = std::sregex_iterator(line.begin(), line.end(), re);
  auto search_end = std::sregex_iterator();

  for (std::sregex_iterator i = search_begin; i != search_end; i++) {
    std::smatch match = *i;
    int value = std::stoi(match.str(1));
    max = std::max(max, value);
  }

  return max;
}

Solver02::Solver02() : Solution(2) {}

Solver02::~Solver02() {}

std::string Solver02::part_1(std::string inputs) {
  std::stringstream ss(inputs);
  std::string line;

  int maxred = 12;
  int maxgreen = 13;
  int maxblue = 14;

  std::regex regame("Game\\s+(\\d+): ");
  std::regex rered("(\\d+) red");
  std::regex regreen("(\\d+) green");
  std::regex reblue("(\\d+) blue");

  uint64_t total = 0;
  while (std::getline(ss, line, '\n')) {
    int game = find_maximum_value_given_regex(regame, line);
    int red = find_maximum_value_given_regex(rered, line);
    int green = find_maximum_value_given_regex(regreen, line);
    int blue = find_maximum_value_given_regex(reblue, line);

    if (red <= maxred && green <= maxgreen && blue <= maxblue) {
      total += game;
    }
  }

  return std::to_string(total);
}

std::string Solver02::part_2(std::string inputs) {
  std::stringstream ss(inputs);
  std::string line;

  std::regex rered("(\\d+) red");
  std::regex regreen("(\\d+) green");
  std::regex reblue("(\\d+) blue");

  uint64_t total = 0;
  while (std::getline(ss, line, '\n')) {
    int red = find_maximum_value_given_regex(rered, line);
    int green = find_maximum_value_given_regex(regreen, line);
    int blue = find_maximum_value_given_regex(reblue, line);

    total += red * green * blue;
  }

  return std::to_string(total);
}
