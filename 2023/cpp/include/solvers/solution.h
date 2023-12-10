#ifndef __AOC_SOLUTION_H__
#define __AOC_SOLUTION_H__

#include <string>

class Solution {
protected:
  int day;

public:
  Solution(int day);
  virtual ~Solution();
  virtual std::string part_1(std::string inputs);
  virtual std::string part_2(std::string inputs);
};

#endif
