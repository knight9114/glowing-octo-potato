#include <map>
#include "registry.h"
#include "d01.h"
#include "d02.h"
#include "solution.h"

Registry::Registry() {
  solutions[1] = new Solver01();
  solutions[2] = new Solver02();
}

Registry::~Registry() {
  for (std::map<int, Solution *>::iterator iter = solutions.begin();
       iter != solutions.end(); iter++) {
    delete iter->second;
  }
  solutions.clear();
}

Solution *Registry::get_solver(int day) { return solutions[day]; }
